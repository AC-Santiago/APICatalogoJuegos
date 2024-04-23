from django.urls import path, re_path
from .views import register, login, delete_account, logout, profile

urlpatterns = [
    re_path(r"register", register),
    re_path(r"login", login),
    re_path(r"profile", profile),
    re_path(r"logout", logout),
    re_path(r"delete_account/(?P<id_usuario>\d+)/", delete_account),
]
