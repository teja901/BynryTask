from django import forms
from .models import CustomerComplaint,Customer

SERVICE_TYPES = [
    ('Gas Leakage', 'Gas Leakage'),
    ('New Connection Request', 'New Connection Request'),
    ('Billing Issue', 'Billing Issue'),
]

class ServiceRequestForm(forms.ModelForm):
    service_type = forms.ChoiceField(choices=SERVICE_TYPES, widget=forms.Select(attrs={'class': 'form-select'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'stateInput', 'placeholder': 'Type to search...'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    document = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomerComplaint
        fields = '__all__'
        exclude=['customer','created_at','ticket_id','status']


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match!")


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")