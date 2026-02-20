from django.urls import path
from .views import MyProfile, HomeView, SignUpView,LoginView, ProfileUpdateView,DashboardView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit" ),
    path("profile/", MyProfile.as_view(), name="profile"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("login/", LoginView.as_view(), name="login" ),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home")
]