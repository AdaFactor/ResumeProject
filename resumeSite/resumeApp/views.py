from django.shortcuts import render, redirect, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from resumeApp.models import Student
from  resumeApp.forms import StudentForm, LetterForm
import numpy as np
import os

template_dir = 'resumeApp/resumeTemplate'
css_dir = os.getcwd() + '/resumeApp/static/css'
fonts_dir = os.getcwd() + '/resumeApp/static/fonts'

test_id = Student.objects.all()[0].id
# test_id = 1

def query_student(id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
    }
    return context


def index(request):
    return render(request, 'resumeApp/index.html')


def templates(request, template_no):
    '''
        View for templates
    '''
    try:
        respones_html = ''.join([template_dir, template_no, '.html'])
        context = query_student(test_id)
        context.update({'template_no': template_no})
        return render(request, respones_html, context)
    except TemplateDoesNotExist:
        return redirect('/templates/view/resume')


def to_pdf(request, template_no):
    '''
        Generate PDF file
    '''
    context = query_student(test_id)
    context.update({
        'template_no': template_no,
        'is_pdf_view': True
    })
    html_file = ''.join([template_dir, template_no, '.html'])
    html_string = render_to_string(html_file, context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(css_dir + '/screens/template'+template_no+'_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response


def cv(request, cv_lang, cv_id):
    '''
        View for CVs
    '''
    context = query_student(test_id)
    letter = context['student'].letter.get(id=cv_id)

    if cv_lang == 'en':
        respons_html = ''.join(['resumeApp/cv_en.html'])
    else:
        respons_html = ''.join(['resumeApp/cv_th.html'])
    context.update({
        'cv_lang': cv_lang,
        'cv_id': cv_id,
        'letter': letter
    })

    return render(request, respons_html, context)


def to_pdf_cv(request, cv_lang, cv_id):
    '''
        Generata pdf for CVs
    '''
    context = query_student(test_id)
    letter = context['student'].letter.get(id=cv_id)
    context.update({
        'cv_lang': cv_lang,
        'cv_id': cv_id,
        'letter': letter,
        'is_pdf_view': True
    })

    html_file = ''.join(['resumeApp/cv_', cv_lang, '.html'])
    font_config = FontConfiguration()
    html_string = render_to_string(html_file, context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(fonts_dir + '/thsarabunnew.css', font_config=font_config),
        CSS(css_dir + '/screens/cv_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css, font_config=font_config)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'

    return response


def view_doc(request, doc_type):
    context = query_student(test_id)
    html_file = ''.join(['resumeApp/view_', doc_type, '.html'])
    context.update({
        'number_of_template': np.arange(1, 4)
    })
    
    return render(request, html_file, context)
    

def new_doc(request, doc_type):
    if request.POST:
        if doc_type == 'resume':
            cform = StudentForm(request, data=request.POST)
        else:
            cform = LetterForm(request, data=request.POST)

        if cform.is_valid():
            cform.save()
            return redirect('resumeApp:view_doc', doc_type=doc_type)

    html_file = ''.join(['resumeApp/new_', doc_type, '.html'])
    if doc_type == 'resume':
        form = StudentForm(request)
    else:
        form = LetterForm(request)
    return render(request, html_file, {'form': form})
    
