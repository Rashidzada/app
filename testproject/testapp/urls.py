from django.urls import path
from .views import*
urlpatterns = [
    path('',index, name='index'),
<<<<<<< HEAD
    path('about/', about, name='about'),
    path('about', about, name='about'),
    path('contact',contact,name='contact'),
=======
    path('about', about, name='about'),
    path('contact',contact,name='contact')
>>>>>>> 3827bffa822984efce8cb40351b99fc5a8a7d7c2
]
