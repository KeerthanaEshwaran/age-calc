from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def home(request):
    return render(request,'home.html')

def addition(request):
    return render(request,'addition.html')
def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
def result(request):
    year=int(0 if request.GET['num1']=="" else request.GET['num1'])
    month=int(0 if request.GET['num2']=="" else request.GET['num2'])
    day=int(0 if request.GET['num3']=="" else request.GET['num3'])
    return render(request,'result.html',{'summation':age(date(year,month,day))})
