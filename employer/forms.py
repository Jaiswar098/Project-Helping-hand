from django import forms
from .models import Person

class   PersonForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':20}))
    class Meta:
        model = Person
        fields = ('image','title','firstname','lastname','email','phone','address',
                  'city','state','pincode')
    
    