from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from .models import Profile
from .forms import ProfileForm, SignUpForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import send_mail
from django.conf import settings
from django_project.email import EmailService

class HomeView(TemplateView):
				template_name = "home.html"

class SignUpView(CreateView):
				form_class = SignUpForm
				template_name = "accounts/register.html"
				success_url = reverse_lazy("email_sent")
				
				def form_valid(self, form):
								user = form.save(commit=False)
								user.is_active = False
								user.save()
								
								uid = urlsafe_base64_encode(force_bytes(user.pk))
								token = default_token_generator.make_token(user)
								verification_link = self.request.build_absolute_uri(
								        reverse(
                "verify_email",
                kwargs={
                    "uidb64": uid,
                    "token": token
                }
            )
        )
        
								EmailService.send_verification_email(
            user,
            verification_link
        )
        
								self.object = user
								
								return redirect(self.get_success_url())
          
        
class EmailSentView(TemplateView):
				template_name = "accounts/email_sent.html"
				
class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):

            if not user.is_active:
                user.is_active = True
                user.save()

            login(request, user)
            return redirect("dashboard")

        return redirect("login")   
        
class LoginView(View):
				def get(self, request):
								form = LoginForm()
								return render(request, "accounts/login.html", {"form": form})
				
				def post(self, request):
								form = LoginForm(request.POST)
								
								if form.is_valid():
												email = form.cleaned_data["email"]
												password = form.cleaned_data["password"]
												
												try:
																user_obj = User.objects.get(email=email)
												except User.DoesNotExist:
																form.add_error(None, "Inavalid craditional")
																return render(request, "accounts/login.html", {"form": form})
												
												user = authenticate(request, username=user_obj.username, password=password)
												
												if user:
																login(request, user)
																return redirect("dashboard")
												
												form.add_error(None, "Inavalid cradition")
								
								return render(request, "accounts/login.html", {"form": form})
													
class DashboardView(LoginRequiredMixin, TemplateView):
				template_name = "accounts/dashboard.html"
	
class MyProfile(LoginRequiredMixin, DetailView):
				model = Profile
				form_class = ProfileForm
				template_name = "accounts/profile.html"
				
				def get_object(self):
								return self.request.user.profile
				
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
				model = Profile
				form_class = ProfileForm
				template_name = "accounts/profile_edit.html"
				
				def get_object(self):
								return self.request.user.profile
				
				def get_success_url(self):
								return reverse_lazy("profile")
								