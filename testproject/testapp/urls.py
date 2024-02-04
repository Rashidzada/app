from django.urls import path
from .views import*
urlpatterns = [
    path('',index, name='index'),
<<<<<<< HEAD
    path('about/', about, name='about'),
=======
    path('about', about, name='about'),
    path('contact',contact,name='contact')
>>>>>>> de4eed097d070f74875ceb87fe9be01a47c63f1b
]
