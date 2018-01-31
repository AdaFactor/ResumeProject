from django.urls import path
from . import views

app_name = 'AuthenApp'
urlpatterns = [
    path('login/', views.login, name='login'),
]
