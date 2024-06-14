from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('sports/', views.sports_view, name='sports'),  # Sports page
]
