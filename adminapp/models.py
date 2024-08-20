# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
class Basemodal(models.Model):
    
    is_deleted = models.BooleanField(default=False)
    everything= models.Manager()  #return all
    objects=NonDeleted() 
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True

class Blog(Basemodal):
    auther_name = models.CharField(max_length=100, null=True, db_index=True)
    date = models.DateField()
    image =  models.FileField(upload_to="Blog_image", null=True,blank=True, db_index=True)
    title = models.CharField(max_length=100, null=True, db_index=True)
    description= models.CharField(max_length=100, null=True, db_index=True)
    status=models.BooleanField(default=False)


class Service(Basemodal):

    title = models.CharField(max_length=100, null=True, db_index=True)
    description= models.CharField(max_length=100, null=True, db_index=True)
    image=  models.FileField(upload_to="Service_image", null=True, db_index=True)
    status=models.BooleanField(default=False)


    
