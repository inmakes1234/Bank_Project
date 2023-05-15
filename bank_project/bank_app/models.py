from django.db import models

# Create your models here.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey




class District(models.Model):
    Dist_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Dist_name


class Branches(models.Model):
    sub_name = models.CharField(max_length=250)
    Dist_name = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name


class Account_application(models.Model):
    firstname = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    phn = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branches,on_delete=models.CASCADE,null=True)
    SAVINGS = 'SA'
    CURRENT = 'CU'
    FIXED_DEPOSIT = 'FD'
    MONEY_MARKET = 'MM'
    CHEQUE = 'CH'

    ACCOUNT_TYPE_CHOICES = [
        (SAVINGS, 'Savings Account'),
        (CURRENT, 'Current Account'),
        (FIXED_DEPOSIT, 'Fixed Deposit Account'),
        (MONEY_MARKET, 'Money Market Account'),
        (CHEQUE, 'Cheque Account'),
    ]
    account_type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPE_CHOICES,
        default=SAVINGS,
    )
    has_debit_card = models.BooleanField(default=False)
    has_credit_card = models.BooleanField(default=False)
    has_cheque_book = models.BooleanField(default=False)
    has_adhaar_card = models.BooleanField(default=False)
    has_pan_card = models.BooleanField(default=False)
