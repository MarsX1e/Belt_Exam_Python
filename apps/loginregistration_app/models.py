# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
# Create your models here.
class UserManangement(models.Manager):
    def checklogin(self,postData):
        error={'status':True,'user':None}
        user=self.filter(email=postData['email'])
        if not len(user):
            error['status']=False
        else:
            if bcrypt.checkpw(postData['password'].encode(),user[0].password.encode()):
                error['user']=user[0]
        return error
    def creation(self,postData):
        user=self.create(
            name=postData['name'],
            alias=postData['alias'],
            email=postData['email'],
            password=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt()),
            bday=postData['bday']
        )
        return user
    def validation(self,postData):
        print 'inmodelnow'
        error=[]
        if len(postData['name'])<2 or postData['name'].startswith(' ') or postData['name'].endswith(' '):
            error.append('User name must be longer than 3 letters, and it can not  start with or end with space')
        if len(postData['alias'])<2 or postData['alias'].startswith(' ') or postData['alias'].endswith(' '):
            error.append('User alias must be longer than 3 letters, and it can not  start with or end with space')
        if not re.match('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',postData['email']):
            error.append('You have to enter a valid email address')
        if len(self.filter(email=postData['email'])):
            error.append('Email has been registrated')
        if len(postData['password'])<8 or postData['password'].isspace():
            error.append('Password must be at least 8 charters and can not be only contain spaces')
        if postData['password']!=postData['conformpw']:
            error.append('Password must be the same as confirming password')
        if not len(postData['bday']):
            error.append('Date of Birth can not be empty.')
        return error
class User(models.Model):
    name=models.CharField(max_length=200)
    alias=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    bday=models.CharField(max_length=200)
    friends=models.ManyToManyField('self')
    objects=UserManangement()
    def __repr__(self):
        return "<User object: {} {}>".format(self.name, self.email)