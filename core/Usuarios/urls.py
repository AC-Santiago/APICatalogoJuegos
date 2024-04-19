from django.urls import path, re_path
from .views import register

urlpatterns = [
    re_path(r"register", register),
]
