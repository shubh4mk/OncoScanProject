from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def doctor_dashboard(request):
    return render(request, 'doctorApp/doctor_dashboard.html')