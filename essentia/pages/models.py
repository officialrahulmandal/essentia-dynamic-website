from django.db import models
from uuid_upload_path import upload_to



class Careers(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    resume = models.FileField(upload_to=upload_to, null=True)
    linked_in = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    stack_overflow = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
