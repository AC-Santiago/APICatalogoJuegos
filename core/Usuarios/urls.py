from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register,
    delete_account,
    profile,
    edit_user,
    send_verification_email_user_resgister,
    send_verification_email_user_chance_password,
    verify_email,
    change_password,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "email/register/send_code/",
        send_verification_email_user_resgister,
        name="send_code_register",
    ),
    path(
        "email/change_password/send_code/",
        send_verification_email_user_chance_password,
        name="send_code_change_password",
    ),
    path("email/code_verify/", verify_email, name="email_verify"),
    re_path(r"register/", register),
    re_path(r"profile/", profile),
    re_path(r"delete_account/(?P<id_usuario>\d+)/", delete_account),
    re_path(r"edit_user/", edit_user),
    re_path(r"change_password/", change_password),
]
