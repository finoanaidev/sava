from django import forms
from django.contrib.auth.models import User

class SellerRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

        # Ensure the email is unique
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email already exists')

        return cleaned_data
