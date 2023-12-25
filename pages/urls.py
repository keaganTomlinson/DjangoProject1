# pages/urls.py

from django.urls import path
from pages import views
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),  # Set project_index as the default homepage
    path("<int:pk>/", views.project_detail, name="project_detail"),
]