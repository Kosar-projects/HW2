from django.shortcuts import render
from rest_framework.response import Response
from jobs.models import Job,Application
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from jobs.serializers import ViewJobSerializer,NewUserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class AddNewEmployee(APIView):
    def post(self,request):
        data=request.data
        result=NewUserSerializer(data=data)
        if(result.is_valid(raise_exception=True)):
            name=data['username']
            password=data['password']
            print("herhe")
            client=authenticate(username=name,password=password)
            if client != None:
                return Response({"status":"the client already exist"})
            print("herhe")

            User.objects.create_user(username=name,password=password)
            return Response({"status":"create new user"})


class ViewAllJobs(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Job.objects.all()
    serializer_class=ViewJobSerializer


class RequestApplication(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        if request.user.is_superuser:
            return Response({"status":"You can't register for application"})
        data=request.data
        job_id=data['job_id']
        job=Job.objects.get(id=job_id)
        Application.objects.create(job=job,applicant=request.user)
        return Response({"status":"you successfully apply for this job"})
    

#handel by the admin panel

# class EditJobDetails(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         data=request.data
#         status=PostIdSerializer(data=data)
#         if status.is_valid(raise_exception=True):
#             if not Job.objects.filter(id=data['post_id']):
#                 return Response({"status":"The post you are looking for doesn't exist"})
#             job=Job.objects.get(id=data['post_id'])
#             if job.company==request.user:
#                 a=UpdateJobInfoSerializer(instance=job,data=data)
#                 a.is_valid(raise_exception=True)
#                 a.save()
#                 return Response("changes applied")

# def post_new_add(data, job_offer):
#     title=data['title']  
#     description=data['description']
#     salary=data['salary'] 
#     expiration_date=data['expiration_date']
#     work_hour_per_day=data['work_hour_per_day'] 
#     Job.objects.create(title=title,description=description,salary=salary,expiration_date=expiration_date,work_hour_per_day=work_hour_per_day,
#                     company=job_offer)
    

# class RegisterJobAd(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         if not request.user.is_superuser:
#             return Response({"status" : "you are not allowed to post a job_ad"})
#         data=request.data
#         result=JobSerializer(data=data)
#         if(result.is_valid(raise_exception=True)):
#             post_new_add(result.data,request.user)
#             return Response({"status":"create the ad"})
