from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.text