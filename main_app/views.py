from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth , Group

# Create your views here.
def index(request):
    return render(request,'index.html')


def teachingAids(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return redirect('/accounts/login')

def dashboard(request):
    return render(request,'dashboard.html')