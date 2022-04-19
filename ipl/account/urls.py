from django.urls import path, re_path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='/login'), name='home'),
    re_path('login/?$', LoginView.as_view(), name='login'),
    re_path('logout/?$', LogoutView.as_view(), name='logout'),
    re_path('password/forgot/?$', ForgotPassword.as_view(), name='forgot_password'),
    re_path('password/reset/(?P<reset_key>[^/]+)?/?$', SetPassword.as_view(), name='set_password'),
]