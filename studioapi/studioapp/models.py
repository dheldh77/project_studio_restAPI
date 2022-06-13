from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName


class MerchantInfo(models.Model):
    merchantId = models.AutoField(primary_key=True)
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=3000, null=True)
    address = models.CharField(max_length=256)
    number = models.CharField(max_length=256, null=True)
    website = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class ExternalUrl (models.Model):
    linkId = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(MerchantInfo,
                                   on_delete=models.CASCADE)
    externalUrl = models.CharField(max_length=256)

    def __str__(self):
        return self.externalLink


class Photo(models.Model):
    photoId = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(MerchantInfo,
                                   on_delete=models.CASCADE)
    photoUrl = models.CharField(max_length=3000)

    def __str__(self):
        return self.photoLink


class MerchantLocation(models.Model):
    locationId = models.AutoField(primary_key=True)
    merchant = models.OneToOneField(MerchantInfo, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    latitute = models.DecimalField(max_digits=10, decimal_places=3)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
