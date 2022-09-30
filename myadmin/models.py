from unicodedata import name
from django.db import models

class CourseDetails(models.Model):
    course_name = models.CharField(max_length=25)
    university = models.CharField(max_length=25)

    def __str__(self):
        return self.course_name
