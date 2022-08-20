from django.contrib import admin
from app.models import Patients

class PatientsAdmin(admin.ModelAdmin):
    list_display= ['name', 'phone','email','gender','created_at']
    search_fields= ['name', 'phone','email','created_at']
    list_per_page = 4
    list_filter=['gender']


admin.site.register(Patients, PatientsAdmin)