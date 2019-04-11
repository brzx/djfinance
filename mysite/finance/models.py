from django.db import models
from djfauth import models as authmodel

# Create your models here.
class AssetType(models.Model):
    assetname = models.CharField(max_length=200)
    detailtype = models.CharField(max_length=200)
    create_dt = models.DateField('created date')
    update_dt = models.DateTimeField('updated date', auto_now=True, null=True)
    
    def __str__(self):
        return self.assetname

class Asset(models.Model):
    user = models.ForeignKey(authmodel.User, on_delete=models.CASCADE)
    as_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    as_iden = models.CharField(max_length=200)
    as_organ = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    bill_date = models.CharField(max_length=200, null=True, blank=True)
    repayment_date = models.CharField(max_length=200, null=True, blank=True)
    credit_limit = models.CharField(max_length=200, null=True, blank=True)
    year_rate = models.CharField(max_length=200, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    create_dt = models.DateField('created date')
    update_dt = models.DateTimeField('updated date', auto_now=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.as_type, self.as_iden)

class AccountTurnOver(models.Model):
    ATYPE = (
        ('out', '支出'),
        ('in', '收入'),
        ('exp', '消费'),
    )
    user = models.ForeignKey(authmodel.User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    ac_type = models.CharField(max_length=50, choices=ATYPE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comment = models.CharField(max_length=500)
    create_dt = models.DateField('created date')
    update_dt = models.DateTimeField('updated date', auto_now=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.asset, self.ac_type, self.amount)