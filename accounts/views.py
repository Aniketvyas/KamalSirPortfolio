from django.shortcuts import render , redirect 
from django.contrib.auth.models import User , auth , Group
from django.contrib import messages



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

def logout(request):
    auth.logout(request)
    return redirect('/')