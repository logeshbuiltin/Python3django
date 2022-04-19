from django.db import models
from django.db.models.deletion import CASCADE


def user_directory_path(instance, filename):
    return 'ipl/media/documents/driver/{0}_{1}'.format(instance.name, filename)


class DriverModel(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField(default=None)
    alternate_contact = models.BigIntegerField(default=None)
    family_contact = models.BigIntegerField(default=None, null=True, blank=True)
    date_of_joining = models.DateField(default=None)
    license_number = models.CharField(max_length=100)
    license_document = models.FileField(upload_to=user_directory_path)
    address_permanent = models.CharField(max_length=300, default=None)
    address_temporary = models.CharField(max_length=300, default=None)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Driver'
        get_latest_by = 'created_dtm'
        ordering = ['name']


class TruckModel(models.Model):
    class TruckTypes(models.TextChoices):
        open_type = 'open', ('Open')
        close_type = 'close', ('Close')
    truck_number = models.CharField(max_length=100)
    no_of_wheels = models.IntegerField(default=None)
    model = models.CharField(max_length=100)
    feet = models.IntegerField(default=None)
    mileage = models.IntegerField(default=0, null=True, blank=True)
    manufacture_name = models.CharField(max_length=100)
    manufacture_date = models.DateField(default=None)
    truck_type = models.CharField(max_length=100, choices=TruckTypes.choices, default=None)
    tonnage = models.IntegerField(default=None)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Truck'
        get_latest_by = 'created_dtm'
        ordering = ['truck_number']


class ConsigneeModel(models.Model):
    name = models.CharField(max_length=150)
    contact_number = models.BigIntegerField()
    gstin = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consignee'
        get_latest_by = 'created_dtm'


class ConsignorModel(models.Model):
    name = models.CharField(max_length=150)
    contact_number = models.BigIntegerField()
    gstin = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consignor'
        get_latest_by = 'created_dtm'


class BillModel(models.Model):
    consignor = models.ForeignKey(ConsignorModel, on_delete=CASCADE)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bill'
        get_latest_by = 'created_dtm'


class LoadingChallanModel(models.Model):
    class ConsigneePlaces(models.TextChoices):
        indore = 'indore', ('Indore')
        nagpur = 'nagpur', ('Nagpur')
        pune = 'pune', ('Pune')
        secunderabad = 'secunderabad', ('Secunderabad')

    lc_no = models.AutoField(primary_key=True)
    billing_date = models.DateField(default=None)
    place_of_receipt = models.CharField(max_length=100, default="Coimbatore")
    place_of_delivery = models.CharField(max_length=100, choices=ConsigneePlaces.choices, default=None)
    driver = models.ForeignKey(DriverModel, on_delete=CASCADE)
    vehicle_no = models.ForeignKey(TruckModel, on_delete=CASCADE)
    supplier = models.CharField(max_length=45)
    weight = models.IntegerField(max_length=45)
    vehicle_hire = models.IntegerField()
    advance_amount = models.FloatField()
    balance_amount = models.FloatField()
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'LoadingChallan'
        get_latest_by = 'created_dtm'


class ShippingOrdersModel(models.Model):
    class TaxPayable(models.TextChoices):
        consignee = 'Consignee', ('Consignee')
        consignor = 'Consignor', ('Consignor')
        ipl = 'IPL', ('IPL')

    class PaymentStatus(models.TextChoices):
        to_pay = 'to_pay', ('To Pay')
        tbb = 'tbb', ('To be Billed')
        paid = 'paid', ('PAID')

    class ConsigneePlaces(models.TextChoices):
        indore = 'indore', ('Indore')
        nagpur = 'nagpur', ('Nagpur')
        pune = 'pune', ('Pune')
        secunderabad = 'secunderabad', ('Secunderabad')

    consignor = models.ForeignKey(ConsignorModel, on_delete=CASCADE)
    consignor_gst = models.CharField(max_length=15)
    consignor_place = models.CharField(max_length=100, default="Coimbatore")
    consignee = models.ForeignKey(ConsigneeModel, on_delete=CASCADE)
    consignee_gst = models.CharField(max_length=15)
    consignee_place = models.CharField(max_length=100, choices=ConsigneePlaces.choices, default=None)
    no_of_packages = models.CharField(max_length=100)
    package_value = models.IntegerField(null=True, default=None, blank=True)
    package_description = models.CharField(max_length=1000)
    actual_weight = models.FloatField(default=None, null=True)
    charged_weight = models.FloatField(default=None, null=True)
    amount_per_kg = models.FloatField(default=None, null=True)
    freight_charges = models.FloatField(default=None, null=True, blank=True)
    lr_charges = models.FloatField(default=None, null=True, blank=True)
    hamali_charges = models.FloatField(default=None, null=True, blank=True)
    door_collection = models.FloatField(default=None, null=True, blank=True)
    door_delivery = models.FloatField(default=None, null=True, blank=True)
    other_charges = models.FloatField(default=None, null=True, blank=True)
    total_charges = models.FloatField()
    paid_amount = models.FloatField(default=None, null=True)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=None)
    invoice_no = models.CharField(max_length=100)
    invoice_date = models.DateField(default=None)
    billing_date = models.DateField(default=None)
    gs_tax_payable = models.CharField(max_length=100, choices=TaxPayable.choices, default=None)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)
    loading_challan = models.ForeignKey(LoadingChallanModel, on_delete=CASCADE, default=None, null=True)
    bill = models.ForeignKey(BillModel, on_delete=CASCADE, default=None, null=True)

    class Meta:
        db_table = 'Orders'
        get_latest_by = 'created_dtm'


class PaymentNotificationModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sent = models.DateTimeField(default=False)

    class Meta:
        db_table = 'payment_notification'
        get_latest_by = 'date'


class CashReceiptsModel(models.Model):
    gc_no = models.CharField(max_length=100)
    received_from = models.CharField(max_length=125)
    receipt_date = models.DateField(default=None)
    booked_from = models.CharField(max_length=125)
    booked_to = models.CharField(max_length=125)
    total_amount = models.FloatField()
    payment_status = models.CharField(max_length=100, default="")
    created_dtm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cash_receipts'
