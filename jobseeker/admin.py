from django.contrib import admin
from .models import Person
from .models import Job
from .models import Application
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

    list_display = ('name', 'email', 'phone', 'city',
                    'state', 'pincode', 'education',
                     'created_on', 
                    'updated_on')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    '''Admin View for Application'''

    list_display = ('job', 'person', 'created_on', 'updated_on', 'accepted')