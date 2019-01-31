from django.db import models

# Create your models here.

class Questions_Exam(models.Model):
    question_text=models.CharField(max_length=300, default='')
    answer1 = models.CharField(max_length=300, default='')
    answer2 = models.CharField(max_length=300, default='')
    answer3 = models.CharField(max_length=300, default='')
    answer4 = models.CharField(max_length=300, default='')

class Answer(models.Model):
    pass



