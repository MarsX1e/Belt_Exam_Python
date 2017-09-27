# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def go(request):
    return redirect('/main/')
def index(request):
    return render(request,'loginregistration_app/index.html')
def registration(request):
    print request.POST['name']
    error=User.objects.validation(request.POST)
    if len(error):
        for message in error:
            messages.error(request,message)
        return redirect('/main/')
    user=User.objects.creation(request.POST)
    request.session['name']=request.POST['name']
    request.session['email']=request.POST['email']
    return redirect('/friends/')
def login(request):
    error=User.objects.checklogin(request.POST)
    if error['status']==False:
        messages.error(request,'Email have not been registrated yet')
    else:
        if error['user']:
            user=error['user']
            request.session['name']=user.name
            request.session['email']=user.email
            return redirect('/friends/')
        else:
            messages.error(request,'Password is not correct')
    return redirect('/main/')
def loginout(request):
    request.session.flush()
    return redirect('/main/')