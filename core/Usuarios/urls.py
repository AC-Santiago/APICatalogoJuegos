from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, delete_account, profile, edit_user

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"register/", register),
    re_path(r"profile/", profile),
    re_path(r"delete_account/(?P<id_usuario>\d+)/", delete_account),
    re_path(r"edit_user/", edit_user),
]
