from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:template_no>/', views.templates, name='templates'),
    path('cv/<str:cv_lang>', views.cv, name='cv'),
    path('to_pdf/<str:template_no>/', views.to_pdf, name='to_pdf'),
    path('to_pdf_cv/<str:cv_lang>/', views.to_pdf_cv, name='to_pdf_cv'),
]