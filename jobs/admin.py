from django.contrib import admin

# Register your models here.
from .models import Country, City, Job, Company, Education

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Education)