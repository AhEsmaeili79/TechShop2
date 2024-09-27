from django.db import models
from products.models import Product
from accounts.models import CustomUser
from uuid import uuid4

# Create your models here.


# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = [["cart", "product"]]

    def __str__(self):
        return f"{self.product.name} in {self.cart.user.username}'s cart and quantity of {self.quantity}"
