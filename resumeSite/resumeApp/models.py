from django.db import models
from django.contrib.postgres.fields import ArrayField


class Language(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('e', 'Elementary'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
        ('p', 'Proficiency'),
    )
    user_id = models.IntegerField()
    name = models.CharField(max_length=32)
    level = models.CharField(max_length=1, choices=LEVEL, default='b')

    def extract_data(request):
        data = {
            'user_id': request.user.id,
            'name': request.POST['language_name'],
            'level': request.POST['language_level'],
        }
        return data

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
    user_id = models.IntegerField()
    name = models.CharField(max_length=64)
    level = models.CharField(max_length=1, choices=LEVEL, default='b')

    def __str__(self):
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Letter(models.Model):
    language_choices = (
        ('th', 'Thai'),
        ('en', 'English'),
    )
    position_choices = (
        ('dr', 'ผู้อำนวยการ'),
        ('hr', 'ผู้จัดการฝ่ายทรัพยากรบุคคล'),
        ('ot', 'อื่นๆ โปรดระบุ'),
    )
    user_id = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=128)
    position = models.CharField(max_length=64, choices=position_choices, default='hr')
    position_other = models.CharField(max_length=64, blank=True)
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    contents = models.TextField(max_length=5000)
    date = models.DateField()
    time_period = models.CharField(max_length=32, default="xx/xx - yy/yy")
    attachment = models.ManyToManyField('Attachment', related_name='student_attachment', blank=True)
    language = models.CharField(max_length=2, choices=language_choices, default='TH')
    pub_date = models.DateTimeField(auto_now=True)

    def get_contents(self):
        return filter(None, [ p for p in self.contents.split('#') ])

    def get_th_date(self):
        month = (
            'มกราคม',
            'กุมภาพันธ์',
            'มีนาคม',
            'เมษายน',
            'พฤษภาคม',
            'มิถุนายน',
            'กรกฎาคม',
            'สิงหาคม',
            'กันยายน',
            'ตุลาคม',
            'พฤศจิกายน',
            'ธันวาคม',
        )
        date = self.date
        the_month = month[date.month-1]
        thai_year = date.year + 543
        return ('วันที่ %d %s %d') % (date.day, the_month, thai_year)

    def __str__(self):
        return self.company_name


class Experience(models.Model):
    user_id = models.IntegerField()
    company_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    role = models.TextField(max_length=400, blank=True)
    time_period = models.CharField(max_length=32)


    def get_role_list(self):
        role = self.role
        role_list = filter(None, role.split('#'))
        return role_list

    def __str__(self):
        return self.company_name


class Reference(models.Model):
    user_id = models.IntegerField()
    advisor_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    affiliation = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=10)
    email = ArrayField(models.CharField(max_length=64), size=2, default=list())

    def extract_data(request):
        data = {
            'user_id': request.user.id,
            'advisor_name': request.POST['advisor_name'],
            'position': request.POST['position'],
            'affiliation': request.POST['affiliation'],
            'phone_no': request.POST['phone_no'],
            'email': request.POST['email'].split(','),
        }
        return data

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
    user_id = models.IntegerField()
    academy_name = models.CharField(max_length=64)
    level = models.CharField(max_length=2, choices=LEVEL, default='un')
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    time_period = models.CharField(max_length=32)

    def extract_data(request, major_obj):
        data = {
            'user_id': request.user.id,
            'academy_name': request.POST['academy_name'],
            'level': request.POST['level'],
            'major': major_obj,
            'time_period': request.POST['time_period'],
        }
        return data

    def __str__(self):
        return self.academy_name
    

class Student(models.Model):
    religion_choice = (
        ('b', 'Buddistsm'),
        ('c', 'Christians'),
        ('h', 'Hinduism'),
    )

    gender_choice = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    user_id = models.IntegerField(primary_key=True)
    first_name_th = models.CharField(max_length=32)
    last_name_th = models.CharField(max_length=32)
    first_name_en = models.CharField(max_length=32)
    last_name_en = models.CharField(max_length=32)
    address_th = models.TextField(max_length=640)
    address_en = models.TextField(max_length=640)
    gender = models.CharField(max_length=1, choices=gender_choice)
    phone_no = ArrayField(models.CharField(max_length=10), size=2)
    email = ArrayField(models.CharField(max_length=32), size=2)
    birthday = models.DateField()
    nationality = models.CharField(max_length=16)
    religion = models.CharField(max_length=16, choices=religion_choice, blank=True, null=True)
    age = models.IntegerField(default=0)
    education = models.ManyToManyField('Education', related_name='student_education')
    reference = models.ForeignKey('Reference', on_delete=models.CASCADE)
    language = models.ManyToManyField('Language', related_name='student_language')
    skill = models.ManyToManyField('Skill', related_name='student_skill')
    experience = models.ManyToManyField('Experience', related_name='student_experience')
    activity = models.TextField(max_length=500)
    hobby = models.TextField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile/', default='/static/images/user.png')


    def level_to_number(self, objs):
        numeric_level = {
            'b': 20,
            'e': 40,
            'i': 60,
            'a': 80,
            'p': 100
        }
        origin_objs = [ o for o in objs ]
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

    def get_hobby(self):
        return filter(None, self.hobby.split('#'))

    def get_activity(self):
        return filter(None, self.activity.split('#'))

    def __str__(self):
        return ' '.join([self.first_name_th, self.last_name_th])
    
