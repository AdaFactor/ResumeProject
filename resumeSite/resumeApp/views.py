from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML

template_dir = 'resumeApp/resumeTemplate'

def templates(request, template_no):
    try:
        respones_html = ''.join([template_dir, template_no, '.html'])
        context = {'template_no': 1} 
        return render(request, respones_html, context)
    except TemplateDoesNotExist:
        return redirect(templates, template_no=1)

def to_pdf(request, template_no):
    html_file = ''.join([template_dir, template_no, '.html'])
    html_string = render_to_string(html_file)
    html = HTML(string=html_string)
    html.write_pdf(target="/tmp/mypdf.pdf")

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    return response


def cv(request, cv_lang):
    if cv_lang == 'en':
        respons_html = ''.join(['resumeApp/cv_eng.html'])
    else 
        respons_html = ''.join(['resumeApp/cv_thai.html'])
    
    return render(request, respons_html)
