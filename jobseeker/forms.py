from django import forms
from .models import Person, Job

class   PersonForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':20}))
    class Meta:
        model = Person
        fields = ('image','name','email','phone','address',
                  'city','state','pincode','education','resume',)


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','description','requirements','location',
                  'company_name','company_website','company_logo','is_published',)
        
    
