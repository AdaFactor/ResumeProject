from django.forms import ModelForm, DateInput, modelformset_factory, widgets
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div, Button
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions, StrictButton, InlineField


class DateInput(DateInput):
    input_type = 'date'
    

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['user_id']
        widgets = {
            'birthday': DateInput(),
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
        
        self.fields['education'].queryset =  Education.objects.filter(user_id=request.user.id)
        self.fields['reference'].queryset =  Reference.objects.filter(user_id=request.user.id)
        self.fields['language'].queryset =  Language.objects.filter(user_id=request.user.id)
        self.fields['skill'].queryset =  Skill.objects.filter(user_id=request.user.id)
        self.fields['experience'].queryset =  Experience.objects.filter(user_id=request.user.id)
        self.helper.layout = Layout(
            Fieldset(
                'Resume',
                Div (
                    Div(
                        'profile_image',                        
                        'education',                        
                        FormActions(
                            Button('education', '+ Add Education', css_class="btn-primary",
                                data_toggle="modal", data_target="#myEducation"),
                        ),
                        'language',
                        FormActions(
                            Button('add', '+ Add Language', css_class="btn-primary",
                                data_toggle="modal", data_target="#myLanguage"),
                        ),
                        'first_name_en',
                        'last_name_en',
                        'birthday',
                        'age',
                        'gender',
                        'nationality',
                        'religion',
                        'phone_no',
                        'email',
                        'address_en',
                    css_class='col-lg-5'
                    ),
                    Div(
                        'reference',
                        FormActions(
                            Button('add', '+ Add Reference', css_class="btn-primary",
                                data_toggle="modal", data_target="#myReference"),
                        ),
                        'skill',
                        FormActions(
                            Button('add', '+ Add Skill', css_class="btn-primary",
                                data_toggle="modal", data_target="#mySkill"),
                        ),
                        'experience',
                        FormActions(
                            Button('add', '+ Add Experience', css_class="btn-primary",
                                data_toggle="modal", data_target="#myExperience"),
                        ),
                        'first_name_th',
                        'last_name_th',
                        'address_th',
                        Field(
                            'activity', placeholder="Use # for each activities for example, #Activity1 #Activity2"
                        ),
                        Field(
                            'hobby', placeholder="Use # for each hobbies for example, #Hobby1 #Hobby2"
                        ),
                        css_class='col-lg-6')
                    ,css_class='row-fluid'
                ),
                Submit('save', 'Save', css_class='btn btn-success btn-lg btn-block'),
                css_id="student-form",
                ),    
            )


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

    def __init__(self, request, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)
        self.input_formats = ('%d/%m/%Y',)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = request.path
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        
        self.fields['major'].queryset = Major.objects.filter(user_id=request.user.id)

        self.helper.layout = Layout(
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
                    Field('contents', placeholder="Use # if you want a paragraph break (a new paragraph)"),
                ),
                Submit('save', 'Save', css_class='btn btn-success btn-block'),
                css_id='letter-form'  
            ),            
        )
