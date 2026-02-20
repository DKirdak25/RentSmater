from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from .models import Profile
from .forms import ProfileForm, SignUpForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings

class HomeView(TemplateView):
				template_name = "home.html"

class SignUpView(CreateView):
				form_class = SignUpForm
				template_name = "accounts/register.html"
				success_url = reverse_lazy("dashboard")
				
				def form_valid(self, form):
								print("Before save")
								response = super().form_valid(form)
								login(self.request, self.object)
								print("After save")
								return redirect("dashboard")
								
               
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
								