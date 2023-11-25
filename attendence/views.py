from django.shortcuts import render
from .models import Attendance,register

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request,'attendance_list.html', {'Attendance':attendance})

def book(request):
    if request.method =='POST':
        name=request.POST['firstname']
        emai=request.POST['email']
        user=request.POST['username']
        passs=request.POST['password']
        confirm_pass=request.POST['pass']
        adding_data=register(firstname=name,email=emai,username=user,password=passs,confirm=confirm_pass)
        adding_data.save()
    return render(request,'register.html',{})   




