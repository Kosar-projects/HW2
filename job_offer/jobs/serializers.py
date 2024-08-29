from rest_framework import serializers
from .models import Job, Application
from django.contrib.auth.models import User
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model =Job
        fields=('title','description','salary','expiration_date','work_hour_per_day')


class ViewJobSerializer(serializers.ModelSerializer):
    class Meta:
        model =Job
        fields=('id','title','description','salary','expiration_date','work_hour_per_day','posting_date','company')


class UpdateJobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=('title','description','salary','expiration_date','work_hour_per_day')
        extra_kwargs={
            'title' :{'required' :False},
            'description' :{'required' :False},
            'salary' :{'required' :False},
            'expiration_date' :{'required' :False},
            'work_hour_per_day' :{'required' :False}
        }

class PostIdSerializer(serializers.Serializer):
    post_id=serializers.IntegerField()



class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')