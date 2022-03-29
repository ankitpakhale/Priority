from django.urls import path
from . import views

urlpatterns = [
    # for demo
    path('testing/',views.hello, name='HELLO'),

    # path('signup/',views.SignupView, name='SIGNUP'),
    # path('login/', views.userLogin, name='LOGIN'),
    path('', views.dashboard, name='DASHBOARD'),
    path('logout/', views.userLogOut, name='LOGOUT'), 

    path('about/', views.about, name='ABOUT'), 
    path('contact/', views.contact, name='CONTACT'), 
    path('faqs/', views.faqs, name='FAQS'), 
    path('index/', views.index, name='INDEX'), 
    path('productdetail/', views.productDetail, name='PRODUCTDETAILS'), 
    path('products/', views.products, name='PRODUCT'), 
    path('signup1/', views.SignupView, name='SIGNUP1'), 
    path('login1/', views.userLogin, name='LOGIN1')
]
