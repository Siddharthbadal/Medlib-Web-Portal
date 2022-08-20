from django.contrib import admin
from django.urls import path, include
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path("", views.frontend, name='frontend'),
    
    path('', include('django.contrib.auth.urls')),
    
    
    path("backend/", views.backend, name='backend'),

    path("add_patient", views.add_patient, name='add_patient'),
    path("patient/<str:patient_id>", views.patient, name='patient'),
    path("edit_patient", views.edit_patient, name='edit_patient'),
    path("delete_patient/<str:patient_id>", views.delete_patient, name='delete_patient'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)