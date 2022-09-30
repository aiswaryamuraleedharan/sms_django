from django.shortcuts import render,redirect
from myadmin.forms import CourseDetailsForm
from .models import CourseDetails

def Course(request):
    data = CourseDetails.objects.all()
    form = CourseDetailsForm()
    context ={'data':data,'form':form}
    if request.method == 'POST':
        form1 = CourseDetailsForm(request.POST) 
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,'course.html',context)
