from django import forms
from .models import Users, Contact, FAQ
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label="Password"
    )

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        phone_num = cleaned_data.get("phone_number")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if Users.objects.filter(username = username).exists():
            raise forms.ValidationError("Użytkownik o takiej nazwie już istnieje!")

        if Users.objects.filter(phone_number = phone_num).exists():
            raise forms.ValidationError("Użytkownik z takim numerem telefonu już istnieje")

        if Users.objects.filter(email = email).exists():
            raise forms.ValidationError("Użytkownik z takim adresem email już istnieje")

        if password != confirm_password:
            raise forms.ValidationError("Hasła różnią się od siebie!")

        cleaned_data["password_hash"] = make_password(password)
        return cleaned_data

    def save(self, commit=True):
        # Override save method to use the hashed password and default role
        user = super().save(commit=False)
        user.password_hash = self.cleaned_data['password_hash']
        user.role = 'user'  # Set default role to 'user'
        if commit:
            user.save()
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone', 'email', 'address', 'working_hours']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question','answer']




