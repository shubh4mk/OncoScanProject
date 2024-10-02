from django.shortcuts import render

# Create your views here.
def patient_dashboard(request):
    return render(request, 'patientApp/patient_dashboard.html')