from django.contrib import admin
from .models import Person 
from .models import Job
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

    list_display = ('image','title','firstname','lastname' ,'email','phone','address',
                  'city','state','pincode')
    
@admin.register(Job)
class personAdmin(admin.ModelAdmin):
     list_display =('title','description','requirements','location','company_name','company_logo'
                    ,'is_published','posted_date','user')
    