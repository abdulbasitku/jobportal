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

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):

    job_title = models.CharField(max_length=250)
    job_text = models.TextField()
    #company = models.CharField(max_length=250,null=True,blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True,blank=True) 
    positions = models.IntegerField(null=True,blank=True)
    min_experience = models.IntegerField(null=True,blank=True) 
    max_experience = models.IntegerField(null=True,blank=True)
    email_address = models.EmailField(null=True,blank=True)
    link_to_apply = models.URLField(null=True,blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=True) 
    posting_date = models.DateTimeField('Posting Date')
    last_date_apply = models.DateTimeField(null=True,blank=True)
    #image = models.ImageField(upload_to='images/', null=True,blank=True)
    image_url = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.job_title

        