from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    email=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
class UserManager(models.Manager):
    def validate_registration(self,form_data):
        error=[]
        if len(form_data['first_name'])<3:
            errors.append('first name is too short')
        if len(form_data['last_name'])<3:
            errors.append('last name is too short')
        if len(form_data['password'])<8:
            errors.append('password is too short')
        if form_data['password']!=form_data['confirm']:
            errors.append('password and confirm password must match')
        if len(errors)>0:
            return (False,errors)
        else:
            return (True,errors)
