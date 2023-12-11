from django.urls import path
from . import views

# app_name = "test_s"

urlpatterns = [
    path('test_s/', views.test_s, name='test_s'),
]