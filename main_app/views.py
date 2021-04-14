from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth , Group
from django.db.models import Subquery
from . models import *
from django.core.paginator import Paginator
from django.contrib import messages
import datetime as dt
# Create your views here.
def index(request):
    news = newsAndUpdates.objects.all().order_by('-image')
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
    group = Group.objects.get(user=request.user).name
    if group == 'admin':
        subjects = subject.objects.all()
        students = student.objects.all()
        context={
            'subjects':subjects,
            'home':True,
            'students':students
        }
        return render(request,'dashboard.html',context)
    elif group == 'student':
        stu = student.objects.get(email=request.user)
        subjEnroll = studentEnrollment.objects.filter(student=stu)
        submit = submittedAssignment.objects.filter(submitedBy=stu)
        print(submit)
        data = assignments.objects.filter(subject__in = Subquery(subjEnroll.values('subject'))).exclude(id__in=Subquery(submit.values('assignment')))
        return render(request,'studentDashboard.html',{'data':data,'dataSubjects':subjEnroll,'submited':submit})

def subjectsHome(request):
    subjects = subject.objects.all()
    students = student.objects.all()
    context={
        'subjects':subjects,
        'home':True,
        'students':students,
        'subjectsCheck':True
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
        'studentEnrollment':studentEnrollmentData,
        'navLink':True,
    }
    return render(request,'subjects.html',context)

def addSubject(request):
    if request.method == "POST":
        name = request.POST['name']
        subject(name=name).save()
        return redirect('/subjects')
    
def addStudent(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST['Fname']
        last_name = request.POST['Lname']
        email = request.POST['email']
        university = request.POST['university']
        contact = request.POST['contact']
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists!!')
            return redirect('/subjects')
        else:
            User(
                first_name=first_name,
                last_name = last_name,
                email = email,
            ).save()
            student(
                name = first_name + " "+last_name,
                email = email,
                university = university,
                phoneNumber = contact
            ).save()
        messages.info(request,'User Registerd successfully!!')
        return redirect('/subjects')

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



#------------------ ASSIGNMENT ARENA --------------------------------

def assignmentView(request):
    if Group.objects.get(user=request.user).name == "admin":
        return render(request,'assignments.html')
    else:
        return render(request,'studentAssignment.html')

def createAssignmentView(request):
    data = subject.objects.all()
    return render(request,'assignments.html',{'createAssignment':True,'data':data})

def createAssignmentViewsSecond(request,id):
    return render(request,'assignments.html',{'form':True})

def submitAssignmentData(request,id):
    if request.method == "POST":
        print(request.POST)
        startDate = request.POST['startDate']
        deadlineDate = request.POST['deadline']
        startTime = request.POST['startTime']
        name = request.POST['name']
        deadlineTime = request.POST['deadlineTime']
        assignmentF = request.FILES['ass']
        subjectObj = subject.objects.get(id=id)
        if assignments.objects.filter(startDate = startDate,subject=subjectObj).exists():
            messages.error(request,'Already a assignment is there on'+str(start))
            return redirect('/createAssignments')
        else:
            assignments(
                startDate=startDate,
                deadline = deadlineDate,
                startTime = startTime,
                deadlineTime = deadlineTime,
                subject = subjectObj,
                name=name,
                assignmentFile = assignmentF
            ).save()
            return redirect('/createAssignment')


def viewAssignmentData(request):
    if(Group.objects.get(user=request.user).name == 'admin'):
        data = assignments.objects.all()
        return render(request,'assignments.html',{'data':data,'assignmentView':True})
    else:
        stu = student.objects.get(email=request.user)
        data = assignments.objects.filter(subject__in = Subquery(studentEnrollment.objects.filter(student=stu).values('subject')))
        print(data)
        return render(request,'studentAssignment.html',{'data':data,'assignmentView':True})

def viewSubmissions(request):
    return render(request,'assignments.html',{'viewSubmissions':True})

def submitAssignmentView(request,id):
    if request.method == "POST":
        print(request)
        file = request.FILES['assignmentfile']
        assignment = assignments.objects.get(id=id)
        submitedBy = student.objects.get(email=request.user)
        if submittedAssignment.objects.filter(assignment=assignment,submitedBy=submitedBy).exists():
            messages.error(request,'Assignment already Submited!!')
            return redirect('/dashboard')
        else:
            submittedAssignment(
                submittedFile = file,
                submitedBy = submitedBy,
                assignment = assignment,
                submited_onDate = dt.datetime.now().date(),
                submited_onTime = dt.datetime.now().time()
            ).save()
            return redirect('/dashboard')


def viewSubmissionsView(request,id):
    assignment = assignments.objects.get(id=id)
    submited = submittedAssignment.objects.filter(assignment=assignment)
    print(submited)
    return render(request,'assignments.html',{'data':submited,'submitedAssignmentView':True})