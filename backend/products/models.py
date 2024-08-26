from django.db import models
from accounts.models import CustomUser
from category.models import Category,Brand

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=False)
    count = models.IntegerField(blank=False)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=False)
    brand = models.ForeignKey(Brand,on_delete=models.DO_NOTHING,blank=False)
    model = models.CharField(max_length=255)
    is_favorited_by = models.ManyToManyField(CustomUser,related_name='favorite_products',blank=True)
    main_photo = models.ImageField(upload_to="products/%Y/%m/%d/",blank=False)
    photo1 = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)
    photo2 = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)
    photo3 = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)
    photo4 = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True)


    def __str__(self):
        return f' ProductName: {self.name} Product Category: {self.category.name} Count: {self.count}'