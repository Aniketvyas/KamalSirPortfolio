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
    #----------------------------------------------------
    path('books',views.bookHome)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)