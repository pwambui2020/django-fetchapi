from django.urls import path
from .api import RegistrationAPI, LoginAPI, UserAPI
from knox import views as knox_views
from django.views.generic import TemplateView


urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
#     path('', TemplateView.as_view(template_name="home.html"), name='home'),
]
