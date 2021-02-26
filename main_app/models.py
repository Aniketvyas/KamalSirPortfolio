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