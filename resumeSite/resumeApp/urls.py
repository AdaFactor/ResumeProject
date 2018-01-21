from django.urls import path
from . import views


urlpatterns = [
    path('<str:template_no>/', views.templates, name='templates'),
    path('cv/<str:cv_lang>', views.cv, name='cv'),
    path('to_pdf/<str:template_no>/', views.to_pdf, name='to_pdf'),
]