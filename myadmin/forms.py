from django.forms import ModelForm
from .models import CourseDetails

class CourseDetailsForm(ModelForm):
    class Meta:
        model=CourseDetails
        fields = ['course_name','university']