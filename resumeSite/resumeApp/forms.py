from django.forms import ModelForm, DateInput, modelformset_factory
from .models import Student, Letter, Experience, Education, Reference, Language, Skill
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
            'profile_image': widgets.ClearableFileInput()
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
                        'profile_image',
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
                        'education',
                        FormActions(
                            Button('education', '+ Add Education', css_class="btn-primary",
                                data_toggle="modal", data_target="#myEducation"),
                        ),
                        'reference',
                        FormActions(
                            Button('add', '+ Add Reference', css_class="btn-primary",
                                data_toggle="modal", data_target="#myReference"),
                        ),
                        'language',
                        FormActions(
                            Button('add', '+ Add Language', css_class="btn-primary",
                                data_toggle="modal", data_target="#myLanguage"),
                        ),
                    css_class='col-lg-5'
                    ),
                    Div(
                        'first_name_th',
                        'last_name_th',
                        'address_th',
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
                        'activity',
                        'hobby',
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


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            'academy_name',
            'level',
            'major',
            'time_period',
        ]
    
    def __init__(self, request, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'cv'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Fieldset(
                'Education',
                Field(
                    'academy_name',
                    'level',
                    'major',
                    'time_period',
                ),
                css_id='education-form',                  
            ),
        )
        
class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        fields = [
            'advisor_name',
            'position',
            'affiliation',
            'phone_no',
            'email',
        ]

    def __init__(self, request, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'cv'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Fieldset(
                'Reference',
                Field(
                    'advisor_name',
                    'position',
                    'affiliation',
                    'phone_no',
                    'email',
                ),
                css_id='reference-form',                                                    
            ),
        )

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = [
            'name',
            'level',
        ]

    def __init__(self, request, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'cv'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Fieldset(
                'Language',
                Field(
                    'name',
                    'level',
                ),
                css_id='language-form',                         
            ),
        )

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            'name',
            'level',
        ]

    def __init__(self, request, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'cv'        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Fieldset(
                'Skill',
                Field(
                    'name',
                    'level',
                ),
                css_id='skill-form',                                  
            ),
        )

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            'company_name',
            'position',
            'role',
            'time_period',
        ]
    
    def __init__(self, request, *args, **kwargs):
            super(Experience, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.form_action = 'cv'        
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-6'
            self.helper.layout = Layout(
                Div (
                    Fieldset (
                        'Experiences',
                        Field (
                            'company_name',
                            'position',
                            'role',
                            'time_period',
                        ),
                    ),           
                ),  
            )
