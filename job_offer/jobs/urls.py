from django.urls import path
from jobs.views import ViewAllJobs,RequestApplication
from jobs.views import AddNewEmployee



urlpatterns=[
    # path('hello/',register_job_ad),
    # path('register_job/',RegisterJobAd.as_view()),
    path('view_all_jobs/',ViewAllJobs.as_view()),
    path('request_job/',RequestApplication.as_view()),
    # path('edit_job/',EditJobDetails.as_view()),
    path('sign_up_employee/',AddNewEmployee.as_view())

]