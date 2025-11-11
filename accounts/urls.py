from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterUserView.as_view(), name="register"),
    path("verify-email", views.VerifyUserEmail.as_view(), name="verify-email"),
    path("login", views.LoginUserView.as_view(), name="login"),
    path("test", views.TestAuthenticationView.as_view(), name="test"),
]