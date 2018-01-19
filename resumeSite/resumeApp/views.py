from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.http import Http404

def templates(request, template_no):
    try:
        respones_file = ''.join(['resumeApp/resumeTemplate', template_no, '.html'])
        return render(request, respones_file)
    except TemplateDoesNotExist:
        return redirect(templates, template_no=1)

    
