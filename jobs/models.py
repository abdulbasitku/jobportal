from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Job(models.Model):

    job_title = models.CharField(max_length=250)
    job_text = models.TextField()
    company = models.CharField(max_length=250,blank=True)
    positions = models.IntegerField(blank=True)
    min_experience = models.IntegerField(blank=True) 
    max_experience = models.IntegerField(blank=True)
    email_address = models.EmailField(blank=True)
    link_to_apply = models.URLField(blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=True) 
    pub_date = models.DateTimeField('date published')
    last_date_apply = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.job_title

        