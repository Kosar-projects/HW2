from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicant(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    # is_employee=models.BooleanField(default=False)
