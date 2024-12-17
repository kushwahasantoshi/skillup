from django.contrib import admin
from django.urls import path,include
from skillupapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('aboutUS/', views.aboutus),
    path('courses/', views.coursedetails),
    path('courses/<int:courseid>', views.coursedetails),
    path('contact/', views.contact),
    path('login/',views.login),
    path('register/',views.register),
    
    
    # path('/courses/', views.course_list,name='course_list'),
    # path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # path('submit_quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
    # path('results/<int:submission_id>/', views.view_results, name='view_results'),

    # API for QUestion 
    
    
    path('api/get-quiz/' , views.get_quiz, name='get_quiz')
]