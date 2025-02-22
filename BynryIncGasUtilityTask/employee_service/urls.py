from django.urls import path
from .views import *

urlpatterns = [
   
    path('getAllCustomerComplaints',getAllCustomerComplaints,name='getAllCustomerComplaints'),
    path('update-complaint-status/<int:complaint_id>/', update_complaint_status, name='update_complaint_status'),
    path('getInProgressCustomerComplaints',getInProgressCustomerComplaints,name='getInProgressCustomerComplaints'),
    path('getesolvedCustomerComplaints',getesolvedCustomerComplaints,name='getesolvedCustomerComplaints'),


]