from django.urls import path,include

from . import views
urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('login/',views.login_page,name='login_form'),
    path('signup/',views.signup_page,name='signup_form'),
    path('logout/',views.logout_page,name='logout_form'),
    path('loginValidate/',views.login_validate,name='login_validate'),
    path('signupValidate/',views.,name='signup_process'),
]