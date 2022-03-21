from django import forms
from .models import*


class ApllicationForm(forms.ModelForm):
    class Meta:
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.CharField( min_length=2, max_length=20,attrs={'placeholder': 'Ф.И.О'}),
            'direction':forms.TextInput(required=False, max_length=100, attrs={'placeholder':'direction'}),
            'contact': forms.TextInput(required=False ,max_length=50,attrs={'placeholder': 'contact'}),
            'email': forms.EmailInput(required=False ,max_length=100,attrs={'placeholder': 'email'}),
            'message': forms.Textarea(required=False ,max_length=300 ,attrs={'placeholder': 'message'})
        }