from django import forms 
from .models import Profile

class Profile_creation(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']