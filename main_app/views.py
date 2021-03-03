from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth , Group
from . models import *
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def index(request):
    news = newsAndUpdates.objects.all()
    context = {
        'news':news
    }
    return render(request,'index.html',context)

def gallerys(request):
    galler = gallery.objects.all()
    paginator = Paginator(galler,9)
    page = request.GET.get('page')
    galler = paginator.get_page(page)
    return render(request,'gallery.html',{'gallery':galler})

def teachingAids(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return redirect('/accounts/login')

def dashboard(request):
    subjects = subject.objects.all()
    students = student.objects.all()
    context={
        'subjects':subjects,
        'home':True,
        'students':students
    }
    return render(request,'dashboard.html',context)

def subjectsHome(request):
    subjects = subject.objects.all()
    students = student.objects.all()
    context={
        'subjects':subjects,
        'home':True,
        'students':students
    }
    return render(request,'subjects.html',context)

def subjectDelete(request,id):
    subject.objects.get(id=id).delete()
    return redirect('/subjects')

def subjectUpdate(request,id):
    if request.method == "POST":
        name = request.POST['name']
        subject.objects.filter(id=id).update(name=name)
        return redirect('/subjects')
    else:
        return redirect('/error')

def subjectView(request,id):
    data = studyMaterial.objects.filter(subject=subject.objects.get(id=id))
    print(data)
    if data:
        check = True
    else:
        check = False
    studentEnrollmentData = studentEnrollment.objects.filter(subject=subject.objects.get(id=id))
    print(studentEnrollmentData)
    context={
        'data':data,
        'subjectView':check,
        'studentEnrollment':studentEnrollmentData
    }
    return render(request,'subjects.html',context)

def addSubject(request):
    if request.method == "POST":
        name = request.POST['name']
        subject(name=name).save()
        return redirect('/subjects')
    
def addStudent(request):
    if request.method == "POST":
        studentName = request.POST['name']
        studentEmail = request.POST['email']
        studentUniversity = request.POST['university']
        studentContact = request.POST['contact']
        student(
            name = studentName,
            email = studentEmail,
            university = studentUniversity,
            phoneNumber = studentContact
        ).save()
        return redirect('/dashboard')


def userManager(request):
    users = User.objects.all()
    context={
        'users':users,
        'usersHome' : True
    }
    return render(request,'user.html',context)

def createUser(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        university = request.POST['university']
        phoneNumber = request.POST['phoneNumber']
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists!!')
            return redirect('/userManager')
        else:
            User(
                first_name=first_name,
                last_name = last_name,
                email = email,
            ).save()
            student(
                name = first_name + last_name,
                email = email,
                university = university,
                phoneNumber = phoneNumber
            ).save()
        messages.info(request,'User Registerd successfully!!')
        return redirect('/userManager')

    return render(request,'users.html')

def deleteUser(request,id):
    User.objects.get(id=id).delete()
    messages.info(request,' User Deleted Successfully!!')
    return redirect('/userManager')
def registrationRequests(request):
    data = registrationRequest.objects.all()
    context={
        'data':data,
        'registrationRequest':True
    }
    return render(request,'user.html',context)

def acceptRegistrationRequest(request,id):
    data = registrationRequest.objects.get(id=id)
    User(
        first_name = data.name,
        username = data.email,
        email=data.email,
        is_active = True
    ).save()
    data.delete()
    return redirect('/registrationRequest')

def declineRegistrationRequest(request,id):
    registrationRequest.objects.get(id=id).delete()
    return redirect('/registrationRequest')


#------------------------ Quizes Arena -----------------------------

def quizHome(request):
    return render(request,'quiz.html')

