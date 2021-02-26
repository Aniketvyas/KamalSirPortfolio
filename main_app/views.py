from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth , Group
from . models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

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


def bookHome(request):
    data = subject.objects.all()
    context={
        'data':data
    }
    return render(request,'books.html',context)


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