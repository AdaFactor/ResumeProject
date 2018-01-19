from django.urls import path
from . import views

urlpatterns = [
    path('<str:template_no>/', views.templates, name='templates')
]