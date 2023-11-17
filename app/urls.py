from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup_page",views.signup_page,name="signup_page"),
    path("login_page",views.login_page,name="login_page"),

    path("admin_home",views.admin_home,name="admin_home"),
    path("user_home",views.user_home,name="user_home"),

    path("create_user",views.create_user,name="create_user"),
    path("login_funtion",views.login_funtion,name="login_funtion"),
    path("logout",views.logout,name="logout"),

    
]
