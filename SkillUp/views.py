# from django.http import HttpResponse,HttpResponseRedirect
# from django.shortcuts import render
# from .forms import userForm



# def home(request):
#     data={
#         'title' : 'SkillUP'
#     }
#     return render(request,"index.html",data)

# def aboutus(request):
#     data={
#         'title': 'About-Us'
#     }
#     return render(request,"aboutUS.html",data)

# def courses(request):
#     data={
#         'title': 'Courses'
#     }
#     return render(request,"courses.html",data)


# def coursedetails(request,courseid):
#     return HttpResponse(courseid) 

# def contact(request):
#     data={
#         'title': 'Contact Us'
#     }
#     return render(request,"contact.html",data) 


# def login(request):
#     data={
#         'title': 'Login'
#     }
#     return render(request,"login.html",data) 





# def register(request):
#     username = userForm()
#     fn = userForm()
#     data={'form':fn}
#     try:
#         if request.method=="POST":
#             if request.POST.get('name')=="":
#                 return render(request,'signup.html',{'error':True})
#             # elif eval(request.POST.get('contact')):
#             #     return render(request,'signup.html',{'error':True})
#             elif request.POST.get('email'):
#                 return render(request,'signup.html',{'error':True})
#             # elif request.POST.get('user'):
#             #     return render(request,'signup.html',{'error':True})
            
            
#             name = request.POST.get('name')
#             contact = eval(request.POST.get('contact'))
#             mail = request.POST.get('email')
#             user_type = request.POST.get('user')
#             data={
#                 'name':name,
#                 'contact': contact,
#                 'email': mail,
#                 'user_type':user_type,
#                 'form':fn
#             }
            
#             # return HttpResponseRedirect('/')
#     except:
#        print(e)
#     return render(request,'signup.html',data) 


