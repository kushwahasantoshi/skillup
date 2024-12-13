from django.http import HttpResponse
from django.shortcuts import render
from .forms import userForm


def home(request):
    data={
        'title' : 'SkillUP'
    }
    return render(request,"index.html",data)

def aboutus(request):
    data={
        'title': 'About-Us'
    }
    return render(request,"aboutUS.html",data)

def courses(request):
    data={
        'title': 'Courses'
    }
    return render(request,"courses.html",data)


def coursedetails(request,courseid):
    return HttpResponse(courseid) 

def contact(request):
    data={
        'title': 'Contact Us'
    }
    return render(request,"contact.html",data) 


def login(request):
    data={
        'title': 'Login'
    }
    return render(request,"login.html",data) 



def register(request):
    name = None
    try:
       name = request.POST['name']
       print(name);
    except:
       pass
    return render(request,'signup.html',{'value':name}) 