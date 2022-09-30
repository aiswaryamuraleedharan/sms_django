from django.shortcuts import render,redirect
from .forms import StudentDetailsForm
from .models import StudentDetails

def Register(request):
    data = StudentDetails.objects.all()
    form = StudentDetailsForm()
    context = {'data':data,'form':form}
    if request.method == 'POST':
        form1 = StudentDetailsForm(request.POST) 
        if form1.is_valid():
            form1.save()
            return redirect('stu_register')
    return render(request,'register.html',context)
