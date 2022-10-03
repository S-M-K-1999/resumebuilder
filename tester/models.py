from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from statistics import mode
from xml.parsers.expat import model
from django.db import models
import os

def filepath(request,filename):
    return os.path.join ('media/',filename)
# Create your models here.
class Profile(models.Model):
    #basic
    id = models.AutoField(primary_key=True)
    profileimg = models.ImageField(upload_to = 'images/',null = True, blank = True)
    name = models.CharField(max_length=100,default='')
    lname = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    #address
    address1 = models.CharField(max_length=100,default='')
    address2 = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    zip = models.CharField(max_length=100,default='')

    #Education
    school = models.CharField(max_length=100,default='')
    schoolclass = models.CharField(max_length=100,default='')
    schooly1 = models.CharField(max_length=100,default='')
    schooly2 = models.CharField(max_length=100,default='')

    degree = models.CharField(max_length=100,default='')
    stream = models.CharField(max_length=100,default='')
    university = models.CharField(max_length=100,default='')
    degreein = models.CharField(max_length=100,default='')
    collegey1 = models.CharField(max_length=100,default='')
    collegey2 = models.CharField(max_length=100,default='')
    #projects
    projectheading = models.CharField(max_length=100,default='')
    project_dis = models.CharField(max_length=100,default='')

    #experience
    ex1pos = models.CharField(max_length=100,default='')
    ex1com =models.CharField(max_length=100,default='')
    ex1years = models.CharField(max_length=100,default='')

    ex2pos = models.CharField(max_length=100,default='')
    ex2com =models.CharField(max_length=100,default='')
    ex2years = models.CharField(max_length=100,default='')

    #about
    designation = models.TextField(max_length=1000,default='')
    about = models.TextField(max_length=1000,default='')
    skill = models.TextField(max_length=1000,default='')
    interest = models.TextField(max_length = 1000,default='')

    def __str__(self) :
        return str(self.name)