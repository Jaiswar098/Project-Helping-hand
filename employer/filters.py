import django_filters
from .models import Job
from jobseeker.models import Application, Person

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['icontains'],
            'location': ['icontains'],
            'company_name': ['icontains'],
        }

class ApplicationFilter(django_filters.FilterSet):
    class Meta:
        model = Application
        fields = {
            'job': ['exact'],
            'person': ['exact'],
        }