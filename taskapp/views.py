from django.shortcuts import render,redirect
from .models import Admin,Employee,Users
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import JsonResponse
# Create your views here.



def hello(request):
    return render(request,"taskapp/base.html")

def add_emp(request):
    return render(request,"taskapp/form.html")    

def employe(request):
    data=Employee.objects.all()
    emp={
        "emp_name":data
    }

    return render(request,'taskapp/home.html',emp)   


def users(request):
    data=Users.objects.all()
    emp={
        "user_name":data
    }

    return render(request,'taskapp/users.html',emp)

def admins(request):
    data=Admin.objects.all()
    emp={
        "admin_name":data
    }

    return render(request,'taskapp/admin.html',emp)



def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect ('taskapp:home')
    else:
        form=UserCreationForm()
    return render(request,'taskapp/register.html',{'form':form}) 

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            user=form.get_user()
            login(request,user)
            return redirect('taskapp:users') 
    else:
        form=AuthenticationForm()
    return render(request,'taskapp/login.html',{'form':form})     

def create_post(request):
    posts = Employee.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        img=request.FILES.get('img')
        response_data['name'] = name
        response_data['email'] = email
        response_data['img']=img
      
        Employee.objects.create(
            name = name,
            email= email,
            img=img,
            )
        return JsonResponse(response_data)

    return render(request, 'taskapp/create-post.html', {'posts':posts})   


def logout_view(request):
   if request.method=='POST':
       logout(request)
       return redirect("/")     
