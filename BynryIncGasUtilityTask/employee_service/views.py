from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from customer_service.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def getAllCustomerComplaints(request):
    search_query = request.GET.get('search', '')  # Get search term from request
   
    
    if search_query:
        customersComplaints = CustomerComplaint.objects.select_related('customer').filter(
            Q(ticket_id=search_query) | 
            Q(customer__username__icontains=search_query)
        ).order_by('-id')
    else:
        
         customersComplaints = CustomerComplaint.objects.select_related('customer').order_by('-id')
        
        # elif complaintType=="Inprogress":
        #      customersComplaints = CustomerComplaint.objects.select_related('customer').filter(status="Inprogress").order_by('-id')
        
        # else:
        #      customersComplaints = CustomerComplaint.objects.select_related('customer').filter(status="Resolved").order_by('-id')

    paginator = Paginator(customersComplaints, 1)
    page = request.GET.get('page', 1)

    try:
        complaints = paginator.page(page)
    except PageNotAnInteger:
        complaints = paginator.page(1)
    except EmptyPage:
        complaints = paginator.page(paginator.num_pages)

    return render(request, "EmployeeAllComplaints.html", {
        "complaints": complaints, 
        "paginator": paginator, 
        "search_query": search_query
    })
    
    
def getInProgressCustomerComplaints(request):
    search_query = request.GET.get('search', '')  
   
    
    if search_query:
        customersComplaints = CustomerComplaint.objects.select_related('customer').filter(
            Q(ticket_id=search_query) | 
            Q(customer__username__icontains=search_query)
        ).order_by('-id')
    else:
   
        customersComplaints = CustomerComplaint.objects.select_related('customer').filter(status="Inprogress").order_by('-id')
        
        # else:
        #      customersComplaints = CustomerComplaint.objects.select_related('customer').filter(status="Resolved").order_by('-id')

    paginator = Paginator(customersComplaints, 1)
    page = request.GET.get('page', 1)

    try:
        complaints = paginator.page(page)
    except PageNotAnInteger:
        complaints = paginator.page(1)
    except EmptyPage:
        complaints = paginator.page(paginator.num_pages)

    return render(request, "EmployeeAllComplaints.html", {
        "complaints": complaints, 
        "paginator": paginator, 
        "search_query": search_query
    })


def getesolvedCustomerComplaints(request):
    search_query = request.GET.get('search', '')  
   
    
    if search_query:
        customersComplaints = CustomerComplaint.objects.select_related('customer').filter(
            Q(ticket_id=search_query) | 
            Q(customer__username__icontains=search_query)
        ).order_by('-id')
    else:
   
        customersComplaints = CustomerComplaint.objects.select_related('customer').filter(status="Resolved").order_by('-id')

    paginator = Paginator(customersComplaints, 1)
    page = request.GET.get('page', 1)

    try:
        complaints = paginator.page(page)
    except PageNotAnInteger:
        complaints = paginator.page(1)
    except EmptyPage:
        complaints = paginator.page(paginator.num_pages)

    return render(request, "EmployeeAllComplaints.html", {
        "complaints": complaints, 
        "paginator": paginator, 
        "search_query": search_query
    })




from django.utils.timezone import now





def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(CustomerComplaint, id=complaint_id)

    new_status = request.POST.get("status") 

    if new_status in ["Inprogress", "Resolved"]:
        complaint.status = new_status
        if new_status == "Resolved":
            complaint.resolvedTime = now() 
        complaint.save()
        return JsonResponse({"success": True, "new_status": new_status})

    return redirect("complaints_list")  