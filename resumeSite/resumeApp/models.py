from django.db import models
from django.contrib.postgres.fields import ArrayField


class Address(models.Model):
    address_no = models.CharField(max_length=10)
    village_no = models.CharField(max_length=3)
    alley = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    sub_area = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    postcode = models.CharField(max_length=5)


class Language(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('e', 'Elementary'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
        ('p', 'Proficiency'),
    )
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=1, choices=LEVEL, default='b')


class Skill(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('e', 'Elementary'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
        ('p', 'Proficiency'),
    )
    name = models.CharField(max_length=32)


class Letter(models.Model):
    company_name = models.CharField(max_length=32)
    person_name = models.CharField(max_length=32)
    contents = ArrayField(models.CharField(max_length=500), size=10, default=list())
    date = models.CharField(max_length=32, default="-/-/-")
    time_period = models.CharField(max_length=20, default="xx/xx - yy/yy")
    attachments = ArrayField(models.CharField(max_length=64), size=10, default=list())


class Experience(models.Model):
    company_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    role = models.CharField(max_length=400, blank=True)
    time_period = models.CharField(max_length=32)


class Reference(models.Model):
    advisor_name = models.CharField(max_length=32)
    postion = models.CharField(max_length=32)
    Affiliation = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=10)
    email = ArrayField(models.CharField(max_length=64), size=2, default=list())


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    

class Branch(models.Model):
    branch_name = models.CharField(max_length=64)
    course = models.ForeignKey('Course', on_delete=models.CASCADE,)


class Major(models.Model):
    major_name = models.CharField(max_length=64)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE) 


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
    

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.ManyToManyField('Address', related_name='student_address')
    phone_no = ArrayField(models.CharField(max_length=10), size=2)
    email = ArrayField(models.CharField(max_length=10), size=2)
    birthday = models.CharField(max_length=10)
    nationality = models.CharField(max_length=16)
    religion = models.CharField(max_length=16)
    age = models.IntegerField(default=0)
    education = models.ManyToManyField('Education', related_name='student_education')
    reference = models.ForeignKey('Reference', on_delete=models.CASCADE)
    language = models.ManyToManyField('Language', related_name='student_language')
    skill = models.ManyToManyField('Skill', related_name='student_skill')
    activity = ArrayField(models.CharField(max_length=32), size=10)
    hobbie = ArrayField(models.CharField(max_length=32), size=10)
    letter = models.ManyToManyField('Letter', related_name='student_letter')

    
