from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from weasyprint import HTML, CSS

template_dir = 'resumeApp/resumeTemplate'

def templates(request, template_no):
    try:
        respones_html = ''.join([template_dir, template_no, '.html'])
        context = {'template_no': template_no}
        return render(request, respones_html, context)
    except TemplateDoesNotExist:
        return redirect(templates, template_no=1)


def to_pdf(request, template_no):
    '''
        Generate PDF file
    '''

    html_file = ''.join([template_dir, template_no, '.html'])
    css_dir = os.getcwd() + '/resumeApp/static/css'
    html_string = render_to_string(html_file, {'is_pdf_view': True})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [
        CSS(css_dir + '/screens/common_style.css'),
        CSS(css_dir + '/screens/template'+template_no+'_screen.css'),
    ]
    pdf_file = html.write_pdf(stylesheets=css)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    return response


def cv(request, cv_lang):
    if cv_lang == 'en':
        respons_html = ''.join(['resumeApp/cv_eng.html'])
    else:
        respons_html = ''.join(['resumeApp/cv_thai.html'])
    
    return render(request, respons_html)
