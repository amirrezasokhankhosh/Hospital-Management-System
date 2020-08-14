from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# FOR SHOWING THE HOME VIEW OF APP
def home_view(request):
    return render(request,'hospital/home_view.html')

# FOR SHOWING A PAGE TO SIGN IN OR REGISTER ADMIN
def admin_click_view(request):
    return render(request , 'hospital/admin_click.html')
    
# FOR SHOWING A PAGE TO SIGN IN OR REGISTER DOCTOR
def doctor_click_view(request):
    return render(request , 'hospital/doctor_click.html')

# FOR SHOEING A PAGE TO SIGN IN OR REGISTER PATIENT
def patient_click_view(request):
    return render(request , 'hospital/patient_click.html')

# PAGE FOR SIGN UP THE ADMIN
def admin_signup_view(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = forms.AdminUserForm()
    else:
        # POST data submitted; process data.
        form = forms.AdminUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('admin_login')
    context = {'form': form}
    return render(request, 'hospital/admin_signup.html', context)

# ADMIN DASHBOARD PAGE VIEW
def admin_dashboard_view(request):
    return render(request , 'hospital/admin_dashboard.html')

# DOCTOR SIGN UP PAGE VIEW
def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctor_login')
    return render(request,'hospital/doctor_signup.html',context=mydict)

#DOCTOR DASHBOARD PAGE VIEW
def doctor_dashboard_view(request):
    return render(request , 'hospital/doctor_dashboard.html')

# PATIENT SIGN UP PAGE VIEW
def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patient_login')
    return render(request,'hospital/patient_signup.html',context=mydict)

# PATIENT DASHBOARD PAGE VIEW 
def patient_dashboard_view(request):
    return render(request , 'hospital/patient_dashboard.html')

# CHECK FOR SEND USERS TO THEIR DASHBOARD
def after_login_view(request):
    if is_admin(request.user):
        return HttpResponseRedirect(reverse('hospital:admin_dashboard_view'))
    elif is_doctor(request.user):
        return HttpResponseRedirect(reverse('hospital:doctor_dashboard_view'))
    elif is_patient(request.user):
        return HttpResponseRedirect(reverse('hospital:patient_dashboard_view'))

# CHECKING FUNCTIONS
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()