# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Basemodal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    soft_deleted = models.BooleanField(default=False)

class Blog(models.Model):
  
    auther_name = models.CharField(max_length=100, null=True, db_index=True)
    date = models.DateField()
    image =  models.FileField(upload_to="Blog_image", null=True,blank=True, db_index=True)
    title = models.CharField(max_length=100, null=True, db_index=True)
    description= models.CharField(max_length=100, null=True, db_index=True)
    status=models.BooleanField(default=False)

class Service(models.Model):

    title = models.CharField(max_length=100, null=True, db_index=True)
    description= models.CharField(max_length=100, null=True, db_index=True)
    image=  models.FileField(upload_to="Service_image", null=True, db_index=True)
    status=models.BooleanField()


    
