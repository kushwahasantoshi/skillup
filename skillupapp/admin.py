from django.contrib import admin
from .models import *

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'duration_in_months', 'created_at', 'updated_at')

# @admin.register(Quiz)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('title', 'duration', 'total_marks', 'pass_percentage', 'created_at', 'updated_at')

# @admin.register(UserSubmission) 
# class UserSubmissionAdmin(admin.ModelAdmin):
#     list_display = ('user', 'quiz', 'score', 'submitted_at')


admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Course)

class AnswerAdmin(admin.StackedInline):
    model=Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]
    
admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)