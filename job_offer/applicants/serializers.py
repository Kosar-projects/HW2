from rest_framework import serializers
from .models import Applicant
from django.contrib.auth.models import User


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicant
        fields=('__all__')


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')