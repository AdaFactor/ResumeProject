from django.forms import ModelForm
from .models import Student, Letter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions, StrictButton

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['letter',]
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('save', 'Save', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'birthday',
        )

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = [
            'company_name',
            'person_name',
            'major',
            'contents',
            'date',
            'time_period',
            'attachments',
        ]

    def __init__(self, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('save', 'Save', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        
        self.helper.layout = Layout(
            Div(
                'company_name',
            )
            # Field('company_name'),
        )
        
