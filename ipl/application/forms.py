from django import forms

from django.forms import ModelForm

from .models import *

GENDER_CHOICES = (
    (None, '-None-'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender')
)


class DriverForm(ModelForm):
    class Meta:
        model = DriverModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class TruckForm(ModelForm):
    class Meta:
        model = TruckModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class ConsigneeForm(ModelForm):
    class Meta:
        model = ConsigneeModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class ConsignorForm(ModelForm):
    class Meta:
        model = ConsignorModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class BillForm(ModelForm):
    class Meta:
        model = BillModel
        exclude = ['created_dtm', 'updated_dtm']


class LoadingChallForm(ModelForm):
    class Meta:
        model = LoadingChallanModel
        exclude = ['created_dtm', 'updated_dtm']
        widgets = {
            'billing_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }


class ShippingOrdersForm(ModelForm):
    class Meta:
        model = ShippingOrdersModel
        exclude = ['created_dtm', 'updated_dtm', 'loading_challan', 'bill']
        widgets = {
            'freight_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'lr_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'hamali_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'door_collection': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'door_delivery': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'other_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'total_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control total-charges'
                }
            ),
            'charged_weight': forms.NumberInput(
                attrs={
                    'class': 'form-control freight-calculation'
                }
            ),
            'amount_per_kg': forms.NumberInput(
                attrs={
                    'class': 'form-control freight-calculation'
                }
            )
        }

    def clean(self):
        return self.cleaned_data
