from django import forms
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
				class Meta:
								model = Profile
								fields = ["photo", "user", "birth_date", "bio" ]
								
				def clean_photo(self):
												file = self.cleaned_data.get("photo")
												
												if not file:
																return file
												
												valid_types = ["jpeg", "png"]
												
												ext = file.name.split(".")[-1].lower()
												
												if ext not in valid_types:
																raise ValidationError("Only images files are allowed.")
												
												return file

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
												