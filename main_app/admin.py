from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(student)
admin.site.register(subject)
admin.site.register(studentEnrollment)
admin.site.register(studyMaterial)
admin.site.register(gallery)
admin.site.register(newsAndUpdates)
admin.site.register(registrationRequest)