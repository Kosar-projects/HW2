from django.db import models
from django.contrib.auth.models import User



class Job(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    salary=models.DecimalField(max_digits=10,decimal_places=0)
    posting_date=models.DateTimeField(auto_now_add=True)
    expiration_date=models.DateTimeField()
    work_hour_per_day=models.DecimalField(max_digits=2,decimal_places=0)
    company=models.ForeignKey(User,on_delete=models.CASCADE,related_name='jobs')

class Application(models.Model):
    job=models.ForeignKey(to="jobs.Job",on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    applied_at=models.DateTimeField(auto_now_add=True)


