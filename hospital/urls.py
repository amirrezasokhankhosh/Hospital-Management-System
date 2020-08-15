from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView , LogoutView
urlpatterns = [
    # Home page
    url(r'^$', views.home_view, name='home_view'),

    # SIGN IN OR REGISTER FOR ADMIN
    url(r'^sign_in_register_admin/$' , views.admin_click_view , name='admin_click_view'),

    # SIGN IN OR REGISTER FOR DOCTOR
    url(r'^sign_in_register_doctor/$' , views.doctor_click_view , name='doctor_click_view'),

    # SIGN IN OR REGISTER FOR PATIENT
    url(r'^sign_in_register_patient/$' , views.patient_click_view , name='patient_click_view'),

    # SIGN UP TO ADMIN ACCOUNT
    url(r'^signup_admin/$' , views.admin_signup_view , name='admin_signup_view'),

    # ADMIN HOME PAGE
    url(r'^admin_dashboard/$' , views.admin_dashboard_view , name='admin_dashboard_view'),

    # ADMIN LOGIN
    url(r'^admin_login/$', LoginView.as_view(template_name = 'hospital/admin_login.html'),name='admin_login'),

    # SIGN UP TO DOCTOR ACCOUNT
    url(r'^signup_doctor/$' , views.doctor_signup_view , name='doctor_signup_view'),

    # DOCTOR HOME PAGE
    url(r'^doctor_dashboard/$' , views.doctor_dashboard_view , name='doctor_dashboard_view'),

    # ADMIN LOGIN
    url(r'^doctor_login/$', LoginView.as_view(template_name = 'hospital/doctor_login.html'),name='doctor_login'),

    # SIGN UP TO PATIENT ACCOUNT
    url(r'^signup_patient/$' , views.patient_signup_view , name='patient_signup_view'),

    # PATIENT HOME PAGE
    url(r'^pateint_dashboard/$' , views.patient_dashboard_view , name='patient_dashboard_view'),

    # PATIENT LOGIN
    url(r'^patient_login/$', LoginView.as_view(template_name = 'hospital/patient_login.html'),name='patient_login'),

    # AFTER LOGIN
    url(r'^after_login/$' , views.after_login_view , name='after_login_view'),

    # LOG OUT
    url(r'^logout/$' , LogoutView.as_view(template_name='hospital/home_view.html'),name='logout'),

    # SEE A DOCTOR IN ADMIN DASHBOARD PAGE
    url(r'^admin_dashboard/(?P<doctor_id>\d+)/$', views.admin_doctor_view, name='admin_doctor_view'),

    # ADMIN ADD A DOCTOR
    url(r'^admin_add_doctor/$' , views.admin_add_doctor_view , name='admin_add_doctor_view'),

    # NOT APPROVED DOCTORS 
    url(r'^not_apporved_doctors/$' , views.admin_not_approved_doctors_view , name = 'admin_not_approved_doctors_view'),

    # APPROVE THE DOCTOR
    url(r'^approve_the_doctor/(?P<doctor_id>\d+)/$' , views.approve_doctor_view , name='approve_doctor_view'),

    # REJECT OR DELETE THE DOCTOR
    url(r'^reject_or_delete_the_doctor/(?P<doctor_id>\d+)/$' , views.reject_or_delete_doctor_view , name='reject_or_delete_doctor_view'),
]