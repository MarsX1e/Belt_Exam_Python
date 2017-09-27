# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..loginregistration_app.models import User
from django.shortcuts import render,redirect

# Create your views here.
def friends(request):
    try:
        request.session['email']
    except:
        return redirect('/main/')
    user=User.objects.get(email=request.session['email'])
    other_users=[]
    for person in User.objects.all():
        if user not in person.friends.all() and person!=user:
            other_users.append(person)

    context={
        'user':user,
        'other_users':other_users
    }
    return render(request,'friends_app/friends.html',context)
def user(request,id):
    try:
        request.session['email']
    except:
        return redirect('/main/')
    context={
        'user':User.objects.get(id=id),
        
    }
    return render(request,'friends_app/user.html',context)
def add(request,id):
    try:
        request.session['email']
    except:
        return redirect('/main/')
    user=User.objects.get(email=request.session['email'])
    friend=User.objects.get(id=id)
    user.friends.add(friend)
    print user.friends.all()
    print friend.friends.all()
    
    try:
        request.session['email']
    except:
        return redirect('/main/')
    return redirect('/friends/')
def remove(request,id):
    print 'remove'
    try:
        request.session['email']
    except:
        return redirect('/main/')
    user=User.objects.get(email=request.session['email'])
    friend=User.objects.get(id=id)
    print user.friends.all()
    print friend.friends.all()
    user.friends.remove(friend)
    print user.friends.all()
    print friend.friends.all()
    return redirect('/friends/')