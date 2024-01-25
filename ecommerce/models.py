from django.db import models

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)

    # Add other client-related fields as needed

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add other product-related fields as needed

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # Add other order-related fields as needed

    def __str__(self):
        return f"Order {self.id} - {self.date} - {self.client}"


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    # Add other order line-related fields as needed

    def __str__(self):
        return f"OrderLine {self.id} - {self.order} - {self.product} - {self.quantity}"
