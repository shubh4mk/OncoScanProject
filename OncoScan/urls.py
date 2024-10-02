from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import home
from authentication.views import signin, signup, signout
from adminApp.views import admin_dashboard
from doctorApp.views import doctor_dashboard
from patientApp.views import patient_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('admin_dashboard/', admin_dashboard, name="admin_dashboard"),
    path('doctor_dashboard/', doctor_dashboard, name="doctor_dashboard"),
    path('patient_dashboard/', patient_dashboard, name="patient_dashboard"),
]
