from django.urls import path,include

from . import views
urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('login/',views.login_page,name='login_form'),
    path('signup/',views.signup_page,name='signup_form'),
]