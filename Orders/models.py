from django.db import models
from Products.models import Products
from Accounts.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    total_paid = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سفارش   "
        verbose_name_plural = "سفارش ها"
        ordering = ('-created',)

    def __str__(self):
        return str(self.user.email)


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "جزییات سفارش  "
        verbose_name_plural = "جزییات سفارش ها "

    def __str__(self):
        return self.user.email
