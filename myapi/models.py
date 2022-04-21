from django.db import models

# Create your models here.

class User(models.Model):
    userChoices = (('A', 'Admin'),('U', 'User'))
    firstName = models.CharField(max_length=36)
    lastName = models.CharField(max_length=36)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    userType =  models.CharField(max_length=36, choices=userChoices)

    def __str__(self):
        return self.firstName

    # create/ insert/ add : POST
    # retrieve/ fetch : GET
    # update/ edit : PUT
    # delete/ remove : DELETE




class Inquiry(models.Model):
    intrestedSubjectChoices = (('M', 'Maths'), ('P', 'Physics'), ('C', 'Chemistry'))
    firstName = models.CharField(max_length=36)
    lastName = models.CharField(max_length=36)
    email = models.EmailField(max_length=36)
    contact = models.CharField(max_length=36)
    intrestedSubject = models.CharField(max_length=36, choices=intrestedSubjectChoices)


    def __str__(self):
        return self.firstName


