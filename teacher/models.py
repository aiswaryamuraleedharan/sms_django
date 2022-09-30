from tkinter import CASCADE
from django.db import models
from myadmin.models import CourseDetails

class StudentDetails(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=25)
    course = models.ForeignKey(CourseDetails,on_delete=models.CASCADE)

