from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url='/login')
def homepage(request):
    context = {}
    context = request.user.first_name
    return render(request,'index.html',{'username':context})

def login_page(request):
    return render(request,'login.html')
 
def signup_page(request):
    return render(request,'signup.html')

def logout_page(request):
    logout(request)
    return redirect(login_page)

# def rest_page(request):
#     return render(request,'rest.html')

# def rest_pass(request):
#     user = User.objects.filter(email = request.POST.get('email'))
#     if user:



def login_validate(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    user = authenticate(request,username = username,password = password)
    not_valid = False
    if user is not None:
        print('success')
        login(request,user)
        return redirect(homepage)
    else:
        not_valid = True
        context = {"not_valid":not_valid}
        return render(request,'login.html',context)

def signup_process(request):
    username = request.POST.get("username")                    #Incomplete code.....won't check for unique email !!
    email = request.POST.get("email")
    password = request.POST.get("pass")
    password_confirm = request.POST.get("repeat-pass")
    full_name = request.POST.get("name")
    if password != password_confirm:
        print("Unmatched Password")
        return redirect(signup_page)
    else:
        try:
            new_user = User.objects.create_user(username,email,password)
            new_user.first_name = full_name.split()[0]
            new_user.last_name = full_name.split()[1]
            new_user.save()
            login(request,new_user)
            return redirect(homepage)
        except:
            context = {"not_unique":True}
            return render(request,"signup.html",context)





