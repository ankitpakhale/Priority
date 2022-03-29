from django.urls import path
from . import views

urlpatterns = [
    # for demo
    path('testing/',views.hello, name='HELLO'),

    path('signup/',views.SignupView, name='SIGNUP'),
    path('login/', views.userLogin, name='LOGIN'),
    path('', views.dashboard, name='DASHBOARD'),
    path('logout/', views.userLogOut, name='LOGOUT'), 
    
    path('index/', views.index, name='INDEX'), 
]