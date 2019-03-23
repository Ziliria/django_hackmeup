### iman hasnaouia meskini ###
from django.urls import path

from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('check-login/', views.check_login, name='checklogin'),
    path('health_check/', views.health_check, name='health_check'),
    
]
