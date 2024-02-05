from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')  # Adjust this if necessary
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    else:
        pass

    return render(request, 'contact.html')

def about(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')

        return render(request, 'about.html', {'about': {'image': image, 'title': title, 'description': description}})

    # Add a return statement for the 'GET' request
    return render(request, 'about.html')
