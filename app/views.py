from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from app.models import Patients
from django.http import HttpResponseRedirect, HttpResponse


def frontend(request):
    return render(request, 'app/frontend.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, 'app/backend.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'query' in request.GET:
        q = request.GET['query']
        all_patients_list = Patients.objects.filter(Q(name__icontains =q) | Q(phone__icontains =q) | Q(age__icontains =q)  | Q(gender__icontains =q) | Q(note__icontains =q) | Q(created_at__icontains =q) | Q(email__icontains =q) )
    
    else:
        all_patients_list = Patients.objects.all().order_by('-created_at')
    paginator= Paginator(all_patients_list, 5)
    page = request.GET.get('page')
    all_patients = paginator.get_page(page)

    return render(request, 'app/backend.html', {'patients':all_patients})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
        
        if request.POST.get("name") and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patients()
            
            patient.id = request.POST.get('id')
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.created_at = request.POST.get('created_at')
            
            patient.save()       
            messages.success(request, "Patient added successfully!")
            return HttpResponseRedirect('/backend')
        else:
            return HttpResponseRedirect('/backend')
    else:
        return render(request, 'app/add_patient.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patients.objects.get(id=patient_id)
    if patient != None:
        return render(request, "app/edit_patient.html",{"patient":patient})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_patient(request ):
    if request.method == "POST":
        patient = Patients.objects.get(id= request.POST.get('id'))
        if patient != None:

            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')

            patient.save()

            messages.success(request, 'Patient updated!')
            return HttpResponseRedirect('/backend')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patients.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, 'Patient Deleted!')
    return HttpResponseRedirect('/backend')