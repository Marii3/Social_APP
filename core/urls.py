from django.urls import path

from core.views import index
from . import views



urlpatterns = [ path("", views.index, name = "index"),
                path('signup', views.signup, name = 'signup')]