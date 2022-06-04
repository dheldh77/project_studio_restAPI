from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.categoryName


class MerchantInfo(models.Model):
    merchantId = models.AutoField(primary_key=True)
    categoryId = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    thumbnailId = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    number = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    purchaseCount = models.IntegerField()

    def __str__(self):
        return self.name


class ExternalLink(models.Model):
    linkId = models.AutoField(primary_key=True)
    merchantId = models.ForeignKey(MerchantInfo,
                                   on_delete=models.CASCADE)
    externalLink = models.CharField(max_length=256)

    def __str__(self):
        return self.externalLink


class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    merchantId = models.ForeignKey(MerchantInfo,
                                   on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    review = models.CharField(max_length=3000)
    photoId = models.CharField(max_length=100)

    def __str__(self):
        return self.author
    

class Gallery(models.Model):
    galleryId = models.AutoField(primary_key=True)
    merchantId = models.ForeignKey(MerchantInfo,
                                   on_delete=models.CASCADE)
    photoLink = models.CharField(max_length=3000)

    def __str__(self):
        return self.photoLink
    

class Merchants(models.Model):
    merchantId = models.AutoField(primary_key=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    latitute = models.DecimalField(max_digits=10, decimal_places=3)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name