from django.shortcuts import render , redirect 
from django.contrib.auth.models import User , auth , Group
from django.contrib import messages
from main_app.models import *



# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['email']
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            return redirect('/login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['Password']
        university = request.POST['university']
        phoneNumber = request.POST['phoneNumber']
        if User.objects.filter(email = email).exists():
            messages.error(request,'User Already Exists')
            return redirect('/accounts/register')
        else:
            dataObj = registrationRequest(
                name = name,
                email = email,
                password = password,
                status = "UNDERCONSIDERATION"
            )
            if registrationRequest.objects.filter(email=email).exists():
                messages.error(request,'request already submitted!!')
            else:
                dataObj.save()
                messages.success(request,'registration Successfull!! please Wait for the Confirmation!, you will be able to view teaching aids once you will be accepted by tha ADMIN')
                return redirect('/accounts/register')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')