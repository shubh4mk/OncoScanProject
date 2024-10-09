from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import home
from authentication.views import signin, signup, signout
from adminApp.views import admin_dashboard, doc_verification
from doctorApp.views import doctor_dashboard,upload_doc,success
from patientApp.views import patient_dashboard,upload_patient,success
from chat.views import chat_interface,chat_user
from blog.views import blog_form,blog_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('admin_dashboard/', admin_dashboard, name="admin_dashboard"),
    path('doctor_dashboard/', doctor_dashboard, name="doctor_dashboard"),
    path('patient_dashboard/', patient_dashboard, name="patient_dashboard"),
    path('doc_verification/', doc_verification, name="doc_verification"),
    path('chat_interface/', chat_interface, name="chat_interface"),
    path('chat_user/', chat_user, name="chat_user"),
    path('blog_form/', blog_form, name="blog_form"),
    path('blog_user/', blog_user, name="blog_user"),
    path('upload/', upload_doc, name='upload_doc'),
    path('upload/', upload_patient, name='upload_patient'),
    path('success/', success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)