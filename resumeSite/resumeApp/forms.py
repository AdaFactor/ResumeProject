from django.forms import ModelForm, DateInput
from .models import Student, Letter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions, StrictButton, InlineField


class DateInput(DateInput):
    input_type = 'date'
    

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name_th',
            'last_name_th',
            'address_th',
            'first_name_en',
            'last_name_en',
            'address_en',
            'gender',
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
            'hobby',
            'letter',
        ]
        widgets = {
            'birthday': DateInput()
        }
    
    def __init__(self, request, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'resume'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'

        self.fields['first_name_en'].label = 'Firstname<br>( English )'
        self.fields['last_name_en'].label = 'Lastname<br>( English )'
        self.fields['first_name_th'].label = 'Firstname<br>( Thai )'
        self.fields['last_name_th'].label = 'Lastname<br>( Thai )'
        self.fields['address_en'].label = 'Address<br>( English )'
        self.fields['address_th'].label = 'Address<br>( Thai )'
        self.helper.layout = Layout(
            Fieldset(
                'Resume',
                Div (
                    Div(
                        'first_name_en',
                        'last_name_en',
                        Field('birthday', placeholder="dd/mm/yyyy"),
                        'age',
                        'gender',
                        'nationality',
                        'religion',
                        'phone_no',
                        'email',
                        'address_en',
                        'education',
                        'reference',
                        'language',
                    css_class='col-lg-5'
                    ),
                    Div(
                        'first_name_th',
                        'last_name_th',
                        'address_th',
                        'skill',
                        'experience',
                        'activity',
                        'hobby',
                        css_class='col-lg-6')
                    ,css_class='row-fluid'
                ),
                Submit('save', 'Save', css_class='btn btn-success btn-lg btn-block')
                ),    
            )


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = [
            'company_name',
            'position',
            'position_other',
            'major',
            'language',
            'contents',
            'date',
            'time_period',
            'attachment',
        ]
        widgets = {
            'date': DateInput()
        }

    def __init__(self, request, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'cv'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Div (
                Fieldset (
                    'CV Letter',
                    Field (
                        'language',
                        'major',                 
                        'date',
                        'time_period',
                        'attachment',
                        'position',
                        'position_other',
                        'company_name',
                        'contents',
                    ),
                    Submit('save', 'Save', css_class='btn btn-success btn-block')  
                ),           
            ),  
        )
        
