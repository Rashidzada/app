from django.urls import path
from .views import*
urlpatterns = [
    path('',index, name='index'),

    path('about/', about, name='about'),
    path('about', about, name='about'),
    path('contact',contact,name='contact'),
    path('about', about, name='about'),
    path('contact',contact,name='contact')

]
