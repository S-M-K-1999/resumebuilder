from django.db import models

# Create your models here.
from asyncio.windows_events import NULL
import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    #basic
    id = models.AutoField(primary_key=True)
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
    university = models.CharField(max_length=100,default='')
    degreein = models.CharField(max_length=100,default='')
    collegey1 = models.CharField(max_length=100,default='')
    collegey2 = models.CharField(max_length=100,default='')

    #about
    designation = models.TextField(max_length=1000,default='')
    about = models.TextField(max_length=1000,default='')
    skill = models.TextField(max_length=1000,default='')