from django.views.generic import TemplateView
from django.urls import path, include
from . import views
from .views import SignUpView

app_name = "books"


urlpatterns = [
    path("", views.Home, name="home"),
    path("books/", views.book_list, name="list"),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'),name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
]
