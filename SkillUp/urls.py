"""
URL configuration for skillup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('skillupapp.urls')),
    # path('aboutUS/', views.aboutus),
    
    # path('courses/<int:courseid>', views.coursedetails),
    # path('contact/', views.contact),
    # path('login/',views.login),
    # path('register/',views.register),
    
    
    # path('/courses/', views.course_list,name='course_list'),
    # path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # path('submit_quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
    # path('results/<int:submission_id>/', views.view_results, name='view_results'),
]
