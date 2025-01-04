from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from .forms import BookingForm

# Create your views here.
def index(request):
    # person={
    #     'name':'krishnaprasad',
    #     'age':'21',
    #     'place':'kasaragod'
    # }

    # number={
    #     'num':10
    # }

    number={
        'num':[2,4,5,6,6,7,8,10]
    }
    return render (request,'index.html',number)
def about(request):
    return  render (request,'about.html')
def doctor(request):
    doc_dept={
        'doc':Doctors.objects.all()
    }
    return render (request,'doctor.html',doc_dept)\
    
def department(request):
    dict_depart={
        'dept':Department.objects.all()
    }
    return render (request,'department.html',dict_depart)
def contact(request):
    return render (request,'contact.html')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        form.save()
        return render(request,'confirmations.html')
    form=BookingForm
    dict_forms={
        'forms':form
    }
    return render (request,'booking.html',dict_forms)
