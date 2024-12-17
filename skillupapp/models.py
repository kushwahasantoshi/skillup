from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import uuid

# # User Model

class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    contact=models.IntegerField()
    password = models.CharField(max_length=128, default='default_password')
    use_type=models.CharField(max_length=10)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    
    def __str__(self):
        return self.name
        

# class  BaseModel(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     created_at = models.DateField(auto_now=True)
#     updated_at = models.DateField(auto_now=True)
    
#     class Meta():
#         abstract = True

# # Course Model
# class Category(BaseModel):
#     category = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.category


# class Question(BaseModel):
#     category=models.ForeignKey(Catgoery,related_name='question', on_delete=models.CASCADE)
#     question=models.CharField(max_length=100)
#     marks=models.IntegerField(default=5)

#     def __str__(self):
#         return self.question
    
    
# class Answer(BaseModel):
#     question=models.ForeignKey(Question,on_delete=models.CASCADE ,related_name='answer')
#     answer=models.CharField(max_length=100)
#     is_correct=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.answer



# from django.db import models
# from django.contrib.auth.hashers import make_password, check_password
# import uuid

# User Model
# class Users(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     contact = models.IntegerField()
#     password = models.CharField(max_length=128, default='default_password')
#     use_type = models.CharField(max_length=10)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.name


# Base Model
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Category Model
class Category(BaseModel):
    category= models.CharField(max_length=100)

    def __str__(self):
        return self.category


# Course Model
class Course(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    duration = models.IntegerField(help_text="Duration in months")

    def __str__(self):
        return self.title


# Question Model
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question
    
    def get_answers(self):
        answer_objs = Answer.objects.filter(question = self)
        data = []
        for answe_obj in answer_objs:
            data.append({
                'answeer': answer_objs.answer,
                'is_correct': answer_objs.is_correct
                
            })
        return Answer.objects.filter(question = self)


# Answer Model
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
