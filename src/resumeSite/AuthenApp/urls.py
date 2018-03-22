from django.urls import path
from . import views

app_name = 'AuthenApp'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('authen/', views.authen_view, name='authen_user'),
    path('registration/', views.new_user_view, name='new_user'),
]
