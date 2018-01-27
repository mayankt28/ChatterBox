from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def login_page(request):
    return render(request,'login.html')
 
def signup_page(request):
    return render(request,'signup.html')
