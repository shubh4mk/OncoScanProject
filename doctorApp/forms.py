# forms.py (inside doctorApp or patientApp)
from django import forms

class UploadForm(forms.Form):
    image = forms.ImageField(label='Select an image to upload') 