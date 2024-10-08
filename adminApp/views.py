from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'adminApp/admin_dashboard.html')

@login_required
def doc_verification(request):
    return render(request, 'adminApp/doc_verification.html')