from django.db import models
from django.contrib.postgres.fields import ArrayField


class Address(models.Model):
    address_no = models.CharField(max_length=10)
    village_building = models.CharField(max_length=64, blank=True, null=True)
    village_no = models.CharField(max_length=3)
    alley = models.CharField(max_length=20, blank=True, null=True)
    road = models.CharField(max_length=20, blank=True, null=True)
    sub_area = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    postcode = models.CharField(max_length=5)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' '.join([
        self.address_no, 
        self.village_building,
        'หมู่ '+self.village_no,
        'ต.'+self.sub_area,
        'อ.'+self.area,
        'จ.'+self.province,
        self.postcode
    ])


class Language(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('e', 'Elementary'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
        ('p', 'Proficiency'),
    )
    name = models.CharField(max_length=32)
    level = models.CharField(max_length=1, choices=LEVEL, default='b')

    def __str__(self):
        return self.name


class Skill(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('e', 'Elementary'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
        ('p', 'Proficiency'),
    )
    name = models.CharField(max_length=64)
    level = models.CharField(max_length=1, choices=LEVEL, default='b')

    def __str__(self):
        return self.name


class Letter(models.Model):
    company_name = models.CharField(max_length=128)
    person_name = models.CharField(max_length=64)
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    contents = ArrayField(models.TextField(max_length=1400), size=10, default=list())
    date = models.CharField(max_length=32, default="-/-/-")
    time_period = models.CharField(max_length=32, default="xx/xx - yy/yy")
    attachments = ArrayField(models.CharField(max_length=64), size=10, default=list())
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Experience(models.Model):
    company_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    role = models.TextField(max_length=400, blank=True)
    time_period = models.CharField(max_length=32)


    def get_role_list(self):
        role = self.role
        role_list = filter(None, role.split('-'))
        return role_list

    def __str__(self):
        return self.company_name


class Reference(models.Model):
    advisor_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    affiliation = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=10)
    email = ArrayField(models.CharField(max_length=64), size=2, default=list())

    def __str__(self):
        return self.advisor_name


class Course(models.Model):
    course_name = models.CharField(max_length=64)

    def __str__(self):
        return self.course_name
    

class Branch(models.Model):
    branch_name = models.CharField(max_length=64)

    def __str__(self):
        return self.branch_name


class Major(models.Model):
    major_name = models.CharField(max_length=64)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return ', '.join([self.major_name, self.branch.branch_name, self.course.course_name])


class Education(models.Model):
    LEVEL = (
        ('el', 'Elementary'),
        ('se', 'Secondary'),
        ('un', 'Undergraduate'),
        ('ms', 'Master'),
        ('dr', 'Doctorate'),
    )
    academy_name = models.CharField(max_length=64)
    level = models.CharField(max_length=2, choices=LEVEL, default='un')
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    time_period = models.CharField(max_length=32)

    def __str__(self):
        return self.academy_name
    

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.ManyToManyField('Address', related_name='student_address')
    phone_no = ArrayField(models.CharField(max_length=10), size=2)
    email = ArrayField(models.CharField(max_length=32), size=2)
    birthday = models.CharField(max_length=10)
    nationality = models.CharField(max_length=16)
    religion = models.CharField(max_length=16)
    age = models.IntegerField(default=0)
    education = models.ManyToManyField('Education', related_name='student_education')
    reference = models.ForeignKey('Reference', on_delete=models.CASCADE)
    language = models.ManyToManyField('Language', related_name='student_language')
    skill = models.ManyToManyField('Skill', related_name='student_skill')
    experience = models.ManyToManyField('Experience', related_name='student_experience')
    activity = ArrayField(models.CharField(max_length=32), size=10)
    hobbie = ArrayField(models.CharField(max_length=32), size=10)
    letter = models.ManyToManyField('Letter', related_name='student_letter', blank=True)
    pub_date = models.DateTimeField(auto_now=True)


    def get_m2m_or_empty(self, objs):
        return [] if objs.count() < 1 else [ obj for obj in objs ]


    def get_address(self):
        address = self.address.all()
        return self.get_m2m_or_empty(address)[0]


    def get_experience(self):
        experience = self.experience.all()
        return self.get_m2m_or_empty(experience)


    def get_education(self):
        education = self.education.all()
        return self.get_m2m_or_empty(education)


    def get_letter(self):
        letter = self.letter.all()
        return self.get_m2m_or_empty(letter)


    def level_to_number(self, objs):
        numeric_level = {
            'b': 20,
            'e': 40,
            'i': 60,
            'a': 80,
            'p': 100
        }
        origin_objs = self.get_m2m_or_empty(objs)
        modified_objs = []
        if len(origin_objs) > 0:
            for obj in origin_objs:
                level = obj.level
                obj.level = numeric_level[level]
                modified_objs.append(obj)
        return modified_objs


    def get_skill(self):
        skill = self.skill.all()
        return self.level_to_number(skill)
        

    def get_language(self):
        language = self.language.all()
        return self.level_to_number(language)


    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
    
