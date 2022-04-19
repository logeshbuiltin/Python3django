from django.urls import reverse


def extra_context(request):
    context = {
        "driver_url":reverse('application:driver'),
        "truck_url": reverse('application:truck'),
        "consignee_url": reverse('application:consignee'),
        "consignor_url": reverse('application:consignor'),
        "landingpage_url": reverse('application:landingpage'),
        "loading_challan_url": reverse('application:loadingchallan'),
        "generate_bill_url": reverse('application:billgeneration'),
        "tbb_url": reverse('application:reports')+"?payment_status=tbb",
        "to_pay_url": reverse('application:reports')+"?payment_status=to_pay",
        "paid_url": reverse('application:reports') + "?payment_status=paid",
        "cash_receipt_report_url": reverse('application:cash_receipt_report'),
        "logout_url": reverse('account:logout'),
        "cashreceipt_url": reverse('application:cash_receipt'),
        "order_download_url": reverse('application:order_download')+'?order=1',
        "secondary_user": True if getattr(request.user, "is_secondaryUser", False) else False
    }

    return context