from django.contrib import admin
from resumeApp.models import *


@admin.register(Course)
class GeneralAdmin(admin.ModelAdmin):
    pass


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('major_name', 'branch', 'course')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'address_no',
        'village_building',
        'village_no', 
        'alley',
        'road',
        'sub_area',
        'area',
        'province',
        'postcode', 
        'pub_date',
    )


@admin.register(Language, Skill)
class LanguageAndSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'person_name',
        'contents',
        'date',
        'time_period',
        'attachments',
        'pub_date',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'position',
        'role',
        'time_period',
    )


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'advisor_name',
        'position',
        'affiliation',
        'phone_no',
        'email',
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'academy_name',
        'level',
        'major',
        'time_period',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'phone_no',
        'email',
        'birthday', 
        'nationality', 
        'religion', 
        'age',
        'reference',
        'activity',
        'hobbie',
        'pub_date',
    )