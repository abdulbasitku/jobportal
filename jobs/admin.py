from django.contrib import admin

# Register your models here.
from .models import Country, City, Job

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Job)