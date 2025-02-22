from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from customer_service.forms import  LoginForm, RegistrationForm, ServiceRequestForm
from customer_service.models import Customer, CustomerComplaint

# Create your views here.

def home_page(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        custId=getCustomerId(request)
        if not custId:
            return redirect('customerlogin')
        if form.is_valid():
            
            customer = Customer.objects.get(id=custId) 
            
            complaint = CustomerComplaint(
                customer=customer,
                service_type=form.cleaned_data['service_type'],
                state=form.cleaned_data['state'],
                address=form.cleaned_data['address'],
                document=form.cleaned_data.get('document')
            )
            complaint.save()
            request.session['ticket_id']=complaint.ticket_id
            return redirect('success_page')
        else: print(form.errors,"Error")
    else:
       
        form = ServiceRequestForm()

    return render(request, "CustomerHomePage.html", {'form': form})
    # form = ServiceRequestForm()
    # return render(request,"CustomerHomePage.html",{'form': form})
    
def login_page(request):
    return render(request,"CustomerLoginPage.html")

def success_page(request):
    ticketId=request.session.get('ticket_id')
    return render(request,"SucessPage.html",{'ticket_id':ticketId})

from django.contrib import messages

def customer_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            if Customer.objects.filter(email=email).exists():
                messages.error(request, "User already registered with this email!")
            else:
                customer = form.save(commit=False)
                customer.password = form.cleaned_data["password"] 
                customer.save()
                messages.success(request, "Registration successful! Redirecting to login...")

                return render(request, "CustomeRegister.html", {"form": RegistrationForm(), "success": True})  # Pass success=True

    else:
        form = RegistrationForm()
    
    return render(request, "CustomeRegister.html", {"form": form, "success": False})  # Explicitly set success=False



def customer_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
           
            try:
                customer = Customer.objects.get(email=email,password=password)  
                request.session["customer_id"] = customer.id  
                messages.success(request, "Login successful! Redirecting...")

                return render(request, "CustomerLoginPage.html", {"form": LoginForm(), "success": True})  # Pass success=True

            except Customer.DoesNotExist:
                messages.error(request, "Invalid email or password!")

    else:
        form = LoginForm()
    
    return render(request, "CustomerLoginPage.html", {"form": form})

def getCustomerId(request):
    return request.session.get('customer_id')

def customer_profile(request):
    dataContentType=request.GET.get('type')
    customerId=getCustomerId(request)
    try:
     customer=Customer.objects.get(id=customerId)
    except Customer.DoesNotExist:raise Http404("No Customer Id Found")
    if dataContentType=="All":
        
        data=CustomerComplaint.objects.filter(customer__id=customerId)
    elif dataContentType=="pending":
         data=CustomerComplaint.objects.filter(customer__id=customerId,status="pending")
    elif dataContentType=="Inprogress":
        data=CustomerComplaint.objects.filter(customer__id=customerId,status="Inprogress")
    else:
         data=CustomerComplaint.objects.filter(customer__id=customerId,status="Resolved")
    context={
        'customer':customer,
        'data':data,
        'type':dataContentType,
    }
    return render(request,'CustomerProfile.html',context)


def customer_LogOut(request):
    if request.session.get('customer_id'):
        del request.session['customer_id']
    return redirect('customerlogin')