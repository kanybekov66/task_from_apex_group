from django.db import models

# Create your models here.
class Human(models.Model):
    surname = models.CharField(max_length=36, blank=False, default='f')
    firstName = models.CharField(max_length=36, blank=False, default='f')
    patronymic = models.CharField(max_length=36, blank=False, default='f')
    phoneNumber = models.CharField(max_length=12, blank=False, default='f')
    adress = models.CharField(max_length=36, blank=False, default='f')
    inn = models.CharField(max_length=36, blank=False, default='f')


    def __str__(self):
        return self.surname + ' ' + self.firstName + ' ' + self.patronymic + ', ' + self.adress + ', ' + self.phoneNumber