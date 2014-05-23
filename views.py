from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.utils import simplejson
from django.core.mail import send_mail

from classrooms.models import *


def loginRedirect(request):
    return redirect('/google/auth/')


@login_required
def dashboard(request, classID=False):
    if ClassUser.objects.filter(user=request.user):
        classUser = ClassUser.objects.get(user=request.user)
    else:
        #create a classUser
        classUser = ClassUser.objects.create(
            user = request.user,
            teacher = True,
            readOnly = False,
        )
    
    #Get all users classes
    if classUser.classrooms.all():
        allClasses = classUser.classrooms.all()
    else:
        allClasses = False
        
    
    #Get Trending for the class
    if classID:
        if HashTag.objects.filter(classroomID=classID):
            trendings = HashTag.objects.filter(classroomID=classID).order_by('-timeDate')[:20]
        else:
            trendings = False
    elif allClasses:
        if HashTag.objects.filter(classroomID=allClasses[0].id):
            trendings = HashTag.objects.filter(classroomID=allClasses[0].id).order_by('-timeDate')[:20]
        else:
            trendings = False
    else:
        trendings = False
        
    
    #Get Current Class
    if classID:
        if Classroom.objects.filter(id=classID):
            currentClass = Classroom.objects.get(id=classID)
        else:
            currentClass = False
    elif allClasses:
        currentClass = allClasses[0]
    else:
        currentClass = False
        
    
    #Get Messages
    if currentClass:
        if currentClass.messages.all():
            messages = currentClass.messages.all().order_by('-timeDate')[0:20]
        else:
            messages = False
    else:
        messages = False
    
    return render_to_response('index.html', {
            'user':request.user,
            'classUser':classUser,
            'allClasses':allClasses,
            'trendings':trendings,
            'currentClass':currentClass,
            'messages':messages,
        })











#*******************  Testings Purposes  ***********************************************

def test(request):
    return render_to_response('base.html')














