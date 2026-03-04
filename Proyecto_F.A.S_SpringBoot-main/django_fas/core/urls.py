from django.urls import path

from .views import LandingPageView, LoginView, RegisterView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
