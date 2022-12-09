from django.db import models
from openings.models import Openings


class NewsLetter(models.Model):
    subscribe = models.EmailField(max_length=128)
    objects = models.manager

    def __str__(self):
        return self.subscribe


class Clients(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    logo = models.ImageField(upload_to='clients/', blank=False, null=False)
    objects = models.manager

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=128, null=False, blank=False)
    subject = models.CharField(max_length=128, null=False, blank=False)
    message = models.CharField(max_length=1000, null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.name


class WalkInForm(models.Model):
    opening = models.ForeignKey(Openings, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False, blank=False)
    full_name = models.CharField(max_length=128, null=False, blank=False)
    position_applied = models.CharField(max_length=128, null=False, blank=False)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=128, null=False, blank=False, choices=gender_choices)
    marital_status_choices = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )
    marital_status = models.CharField(max_length=128, null=False, blank=False, choices=marital_status_choices)
    mobile_number = models.CharField(max_length=13, null=False, blank=False)
    current_location = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=128, null=False, blank=False)
    highest_qualification = models.CharField(max_length=128, null=False, blank=False)
    resume = models.FileField(upload_to='resume/', null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.full_name
