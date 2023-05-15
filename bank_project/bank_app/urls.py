from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.home,name='home'),
    path('accountapplication',views.accountapplication,name='accountapplication'),
    path('account_application',views.account_application,name='account_application'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('msg', views.msg, name='msg'),
]