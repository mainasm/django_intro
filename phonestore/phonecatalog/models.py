from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class PhoneMake(models.Model):
    phone_make = models.CharField(max_length=50, unique=True,
                                  help_text='Enter a phone make (e.g. Samsung)')

    def __str__(self):
        return self.phone_make


class Phone(models.Model):
    make = models.ForeignKey(PhoneMake, on_delete=models.RESTRICT)
    phone_name = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50, null=True)
    launch_date = models.DateTimeField('date launched', null=True)
    price = models.IntegerField(default=0)

    KE_SHILLINGS = 'Kshs'
    DOLLAR = 'Dollar'
    EURO = 'Euro'
    BR_POUND = 'Pound'

    CURRENCY_CHOICES = [
        (KE_SHILLINGS, 'Kenya Shillings'),
        (DOLLAR, 'US Dollars'),
        (EURO, 'Euros'),
        (BR_POUND, 'Pounds')
    ]
    sale_currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default=KE_SHILLINGS)
    sku = models.CharField(max_length=5, default=0000, null=False)

    def __str__(self):
        return f'{self.make} {self.phone_name} {self.sale_currency} {self.price}'
