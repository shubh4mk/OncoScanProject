from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, 'adminApp/admin_dashboard.html')