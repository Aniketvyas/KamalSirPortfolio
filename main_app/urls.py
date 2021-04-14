from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('teachingAids',views.teachingAids),
    path('gallery',views.gallerys),

    #------------------------ Dashboard ---------------------
    path('dashboard',views.dashboard),
    path('subjects',views.subjectsHome),
    path('subject/<int:id>/view',views.subjectView),
    path('subject/<int:id>/delete',views.subjectDelete),
    path('subject/<int:id>/update',views.subjectUpdate),
    path('addSubject',views.addSubject),
    path('addStudent',views.addStudent),
# ------------------------- USER MANAGER -----------------------
    path('userManager',views.userManager),
    path('userManager/createUser',views.createUser),
    path('userManager/<int:id>/delete',views.deleteUser),
    path('registrationRequest',views.registrationRequests),
    path('registrationRequest/accept/<int:id>',views.acceptRegistrationRequest),
    path('registrationRequest/decline/<int:id>',views.declineRegistrationRequest),
    path('quizes',views.quizHome),

    #----------------------Assignment URLS --------------------
    path('assignments',views.assignmentView),
    path('createAssignment',views.createAssignmentView),
    path('subject/<int:id>/createAssignment',views.createAssignmentViewsSecond),
    path('subject/<int:id>/submitAssignmentData',views.submitAssignmentData),
    path('viewAssignment',views.viewAssignmentData),
    path('viewSubmission',views.viewSubmissions),
    path('submitAssignment/<int:id>',views.submitAssignmentView),
    path('viewSubmissions/<int:id>',views.viewSubmissionsView)
    #----------------------------------------------------
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)