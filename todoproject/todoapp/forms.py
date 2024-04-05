from .models import task
from django import forms

class todo(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']
