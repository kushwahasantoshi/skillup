from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import random
# from .forms import userForm

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
    # username = userForm()
    # fn = userForm()
    data={}
    try:
        if request.method=="POST":
            if request.POST.get('name')=="":
                return render(request,'signup.html',{'error':True})
            # elif eval(request.POST.get('contact')):
            #     return render(request,'signup.html',{'error':True})
            elif request.POST.get('email'):
                return render(request,'signup.html',{'error':True})
            # elif request.POST.get('user'):
            #     return render(request,'signup.html',{'error':True})
            
            
            name = request.POST.get('name')
            contact = eval(request.POST.get('contact'))
            mail = request.POST.get('email')
            user_type = request.POST.get('user')
            data={
                'name':name,
                'contact': contact,
                'email': mail,
                'user_type':user_type,
            }
            # return HttpResponseRedirect('/')
    except:
       pass
    return render(request,'signup.html',data) 




# from django.shortcuts import get_object_or_404
# from .models import Course, Quiz, UserSubmission
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# import json

# # View for listing courses
# @login_required
# def course_list(request):
#     courses = Course.objects.all()  # You can filter based on the student's interests
#     return render(request, 'learning/course_list.html', {'courses': courses})

# # View to display quiz details and questions
# @login_required
# def quiz_detail(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     return render(request, 'learning/quiz_detail.html', {'quiz': quiz})

# # View to submit answers
# @login_required
# def submit_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)

#     # Process the form submission with user answers
#     if request.method == "POST":
#         user_answers = json.loads(request.body)  # Get user answers as JSON
        
#         # Calculate score
#         score = 0
#         for idx, question in enumerate(quiz.questions_data):
#             user_answer = user_answers[idx].get("selected_option")
#             correct_answer = next(option["option_text"] for option in question["options"] if option["is_correct"])
#             if user_answer == correct_answer:
#                 score += question["marks"]
        
#         # Save submission and score
#         submission = UserSubmission.objects.create(
#             user=request.user,
#             quiz=quiz,
#             score=score,
#             user_answers=user_answers
#         )
#         return JsonResponse({"score": score, "redirect_url": f"/results/{submission.id}/"})

#     return render(request, 'learning/quiz_detail.html', {'quiz': quiz})

# # View to show quiz results
# @login_required
# def view_results(request, submission_id):
#     submission = get_object_or_404(UserSubmission, id=submission_id)
#     return render(request, 'learning/view_results.html', {'submission': submission})


# API For QUESTIONS 

def get_quiz(request):
    try:
        question_obj = list(Question.objects.all())
        data = []
        random.shuffle(question_obj)
        print(question_obj)
        
        for question_obj in question_obj:
            data.append({
                "category":question_obj.category.category,
                "question":question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers()
            })
            
        payload ={'status':True, 'data':data}
        
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    # return HttpResponse("Somthing Went Wrong!")