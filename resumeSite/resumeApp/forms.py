from django.forms import ModelForm
from .models import Student, Letter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions, StrictButton, InlineField

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'address',
            'phone_no',
            'email',
            'birthday',
            'nationality',
            'religion',
            'age',
            'education',
            'reference',
            'language',
            'skill',
            'experience',
            'activity',
            'hobbie',
            'letter',
        ]
    
    def __init__(self, request, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'resume'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Div(
                    'first_name',
                    'last_name',
                    'birthday',
                    'age',
                    'nationality',
                    'religion',
                    'phone_no',
                    'email',
                    'address',
                    'education',
                    'reference',
                    'language',
                    css_class='col-lg-5'
                    ),
                Div(
                    'skill',
                    'experience',
                    'activity',
                    'hobbie',
                    'letter',
                    css_class='col-lg-6')
                ,css_class='row-fluid'
            ),
            Submit('save', 'Save', css_class='btn btn-success btn-lg btn-block')
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
        self.helper.form_action = 'new_doc'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Div (
                Fieldset (
                    'CV Letter',
                    Field (
                        'major',                        
                        'date',
                        'time_period',
                        'attachments',
                        'person_name',
                        'company_name',
                        'contents',
                    ),
                    Submit('save', 'Save', css_class='btn btn-success btn-block')  
                ),           
            ),  
        )
        
