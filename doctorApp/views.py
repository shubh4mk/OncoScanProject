from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UploadForm

@login_required
def doctor_dashboard(request):
    return render(request, 'doctorApp/doctor_dashboard.html')

@login_required
def upload_doc(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Save the image to a directory, or save it in a model field (e.g., ImageField)
            with open(f'media/uploads/{image.name}', 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            return render(request, 'doctorApp/success.html')
    else:
        form = UploadForm()

    return render(request, 'doctorApp/upload.html', {'form': form})

@login_required
def success(request):
    return render(request, 'doctorApp/success.html', {'message': "Upload successful!"})
