from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    accountNumber = models.CharField(max_length=16, default='8888000011112222')
    username = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zipCode = models.CharField(max_length=5, default='12345')
    phoneNumber = models.CharField(max_length=10, default='123456789')

    def __str__(self):
        return self.accountNumber
