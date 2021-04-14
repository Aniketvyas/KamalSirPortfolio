from django.db import models

# Create your models here.

class gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField()
    
class subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    university = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class studentEnrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('student',on_delete=models.CASCADE)
    subject = models.ForeignKey('subject',on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

class studyMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,blank=True)
    uploadDate = models.DateField(auto_now=True)
    attachment = models.FileField()
    subject = models.ForeignKey('subject',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class newsAndUpdates(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    image = models.FileField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class registrationRequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    status = models.CharField(max_length=40)

class assignments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    startDate = models.DateField()
    startTime = models.TimeField()
    deadline = models.DateField()
    deadlineTime = models.TimeField()
    assignmentFile = models.FileField()
    subject = models.ForeignKey('subject', on_delete=models.CASCADE)


class submittedAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey('assignments',on_delete=models.CASCADE)
    submittedFile = models.FileField()
    submitedBy = models.ForeignKey('student',on_delete=models.CASCADE)
    submited_onDate = models.DateField()
    submited_onTime = models.TimeField()