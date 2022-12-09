from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NewsLetter, ContactUs, WalkInForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ["subscribe"]
        widgets = {
            'subscribe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("subscribe")
        if not email:
            raise forms.ValidationError("Please enter your email")
        return email


class WalkInFormForm(forms.ModelForm):
    class Meta:
        model = WalkInForm
        fields = '__all__'

    def save(self, commit=True):
        data = self.cleaned_data
        walk_in = WalkInForm(opening=data['opening'], full_name=data['full_name'], date_of_birth=data['date_of_birth'],
                             gender=data['gender'], highest_qualification=data['highest_qualification'],
                             position_applied=data['position_applied'], mobile_number=data['mobile_number'],
                             marital_status=data['marital_status'], current_location=data['current_location'],
                             email=data['email'], resume=data['resume'])
        walk_in.save()
