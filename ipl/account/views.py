from django.shortcuts import render

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import *
from .models import *
from config.ipl_config import *
import uuid


EMAIL_DOMAIN = "http://localhost"


def does_user_exist(email):
    """
    Checks if a given user exists.
    """
    user_model = get_user_model()
    return user_model.objects.filter(email=email.lower()).exists()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = AccountLoginForm()
        self.context = {
            'form': form,
            "forgot_password_link": reverse("account:forgot_password"),
        }
        return render(request, "Login.html", self.context)

    def post(self, request, *args, **kwargs):
        post_params = self.request.POST.copy()
        email = post_params.get('email').lower()
        user = authenticate(username=email, password=post_params.get('password'))
        if user is not None:
            login(request, user)
            request.session.update({
                'account_login': True
            })
            if request.user.is_secondaryUser:
                return HttpResponseRedirect(reverse('application:to-pay'))
            return HttpResponseRedirect(reverse('application:landingpage'))
        else:
            form = AccountLoginForm(initial={
                'email': email
            })
            self.context = {
                'error': 1,
                'error_msg': "Invalid Credentials",
                'form': form,
                "forgot_password_link": reverse("account:forgot_password"),
            }
            return render(request, "Login.html", self.context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            logout(self.request)
            request.session.update({
                'account_login': False
            })
        form = AccountLoginForm()
        self.context = {
            'form': form,
            'logout': 1,
            "forgot_password_link": reverse("account:forgot_password"),
        }
        return render(request, "Login.html", self.context)

    def post(self, request, *args, **kwargs):
        return LoginView.as_view()(request, *args, **kwargs)


class SetPassword(View):
    def get(self, request, *args, **kwargs):
        form = SetPasswordForm()
        self.context = {
            'form': form
        }
        return render(request, "set_password.html", self.context)

    def post(self, request, *args, **kwargs):
        form = SetPasswordForm(request.POST.copy())
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            try:
                password_object = Passwords.objects.get(email=email, reset_key=kwargs.get("reset_key"))
            except:
                return render(request, "static_content.html", {"invalid_link":1})
            if password_object:
                user_model = get_user_model()
                user = user_model.objects.get(email=email)
                user.set_password(form.cleaned_data.get("password"))
                user.save()
            return HttpResponseRedirect(reverse("account:login"))


class ForgotPassword(View):
    def get(self, request, *args, **kwargs):
        form = ForgotPasswordForm()
        self.context = {
            'form': form
        }
        return render(request, "forgot_password.html", self.context)

    def post(self, request, *args, **kwargs):
        form = ForgotPasswordForm(request.POST.copy())
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            if does_user_exist(email):
                reset_key = str(uuid.uuid4())
                try:
                    obj = Passwords.objects.get(email=email)
                    obj.reset_key = reset_key
                    obj.save()
                except:
                    Passwords.objects.create(email=email, reset_key=reset_key)
                password_reset_link = EMAIL_DOMAIN + reverse("account:set_password", kwargs={'reset_key': reset_key})
                from_email, to = 'purushcs70@gmail.com', 'purushcs70@gmail.com'
                text_content = 'Click on link to finish registration'
                from django.core.mail import send_mail
                send_mail(
                    'IPL: Reset your Password',
                    'ddd',
                    from_email,
                    [to],
                    fail_silently=False,
                    html_message=render_to_string('password_reset_template.html', {'password_reset_link':password_reset_link})
                    ## So you specify the html_message parameter here.
                )
                return render(request, "static_content.html", {"mail_sent":1})