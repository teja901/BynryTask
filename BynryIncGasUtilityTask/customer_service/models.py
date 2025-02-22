from django.db import models

# Create your models here.

class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    
    def __str__(self):
        return self.username

class CustomerComplaint(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='complaints')
    service_type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.TextField()
    document = models.FileField(upload_to='complaints/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ticket_id = models.CharField(max_length=50, unique=True)
    status=models.CharField(max_length=10,default="pending")
    resolvedTime=models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            last_complaint = CustomerComplaint.objects.order_by('-id').first()
            last_number = int(last_complaint.ticket_id.replace("BYRLYN", "")) if last_complaint else 1000
            self.ticket_id = f"BYRLYN{last_number + 1}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_id} - {self.customer.username} - {self.service_type}"