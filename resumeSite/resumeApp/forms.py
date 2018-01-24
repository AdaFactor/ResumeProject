from django.forms import ModelForm
from .models import Student, Letter

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['letter',]

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        exclude = ['pub_date']
        