from django.db import models
from products.models import Product
from accounts.models import CustomUser

# Create your models here.

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,through='CartItem')

    def __str__(self):
        return f"{self.user.username}'s Cart"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} in {self.cart.user.username}'s cart and quantity of {self.quantity}"

