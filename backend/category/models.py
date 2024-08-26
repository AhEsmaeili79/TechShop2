from django.db import models

# Create your models here.
class Category(models.Model):    
    name = models.CharField(max_length=155)
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL,related_name='children')



    class meta:
        verbose_name_plural= "Categories"
    
    def __str__(self):
        return f'{self.name}'
    

class Brand(models.Model):
    name = models.CharField(max_length=155)
    brandimage = models.ImageField(upload_to='brand/%Y/%m/%d/')
    categori = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='brands')

    def __str__(self):
        return f'{self.name}'