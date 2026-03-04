from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'landingpage.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
