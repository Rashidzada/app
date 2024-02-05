from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 233)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()


    def __str__(self):
        return self.name
    
class About(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title