from django.urls import path
from . import views

app_name = 'resumeApp'
urlpatterns = [
    path('<str:template_no>/', views.templates, name='templates'),
    path('cv/<str:cv_lang>/<int:cv_id>', views.cv, name='cv'),
    path('to_pdf/<str:template_no>/', views.to_pdf, name='to_pdf'),
    path('to_pdf_cv/<str:cv_lang>/<int:cv_id>', views.to_pdf_cv, name='to_pdf_cv'),
    path('view/<str:doc_type>', views.view_doc, name='view_doc'),
    path('new/<str:doc_type>', views.new_doc, name='new_doc'),
    path('delete/cv/<int:cv_id>', views.delete_cv, name='delete_cv'),
    path('edit/cv/<int:cv_id>', views.edit_cv, name='edit_cv'),
]