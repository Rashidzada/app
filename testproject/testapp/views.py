from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == ['POST']:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name = name , email = email , subject = subject , message = message)
        return redirect('contact')
    else:
        messages.warning(request,"You mesasage is not sent try again")

    return render(request,'contact.html')