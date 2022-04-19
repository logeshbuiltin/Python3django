import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ipl.settings")

import django
django.setup()

from django.utils import timezone
from django.utils.timezone import localtime

from django.core.mail import send_mail
from django.template.loader import render_to_string

from application.models import ShippingOrdersModel
payment_status = "to_pay"

date_before_14_days = localtime(timezone.now()-timezone.timedelta(days=14)).date()

# result_set = ShippingOrdersModel.objects.filter(payment_status=payment_status, created_dtm__date__lt=date_before_14_days)
result_set = ShippingOrdersModel.objects.all()

send_mail(
    'IPL: TO PAY LIST',
    'ddd',
    "purushcs70@gmail.com",
    ["purushcs70@gmail.com"],
    fail_silently=False,
    html_message=render_to_string('to_pay_notification.html', {"result_set": result_set})
)
