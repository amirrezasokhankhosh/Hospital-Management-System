from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    # Home page
    url(r'^$', views.home_view, name='home_view'),

    # SIGN IN OR REGISTER FOR ADMIN
    url(r'^sign_in_register_admin$' , views.admin_click_view , name='admin_click_view'),

    # SIGN IN OR REGISTER FOR DOCTOR
    url(r'^sign_in_register_doctor$' , views.doctor_click_view , name='doctor_click_view'),

    # SIGN IN OR REGISTER FOR PATIENT
    url(r'^sign_in_register_patient$' , views.patient_click_view , name='patient_click_view'),

    # SIGN UP TO ADMIN ACCOUNT
    url(r'^signup_admin$' , views.admin_signup_view , name='admin_signup_view'),

    # ADMIN HOME PAGE
    url(r'^admin_home$' , views.admin_home_view , name='admin_home_view'),

    # ADMIN LOGIN
    url(r'^admin_login/$', LoginView.as_view(template_name = 'hospital/admin_login.html'),name='admin_login'),

    # SIGN UP TO DOCTOR ACCOUNT
    url(r'^signup_doctor$' , views.doctor_signup_view , name='doctor_signup_view'),

    # ADMIN HOME PAGE
    url(r'^doctor_home$' , views.doctor_home_view , name='doctor_home_view'),

    # ADMIN LOGIN
    url(r'^doctor_login/$', LoginView.as_view(template_name = 'hospital/doctor_login.html'),name='doctor_login'),
]