from django.db import models
from accounts.models import CustomUser
from products.models import Product
# Create your models here.

# Date Shamsi
from django.utils import timezone
from persiantools.jdatetime import JalaliDate
import pytz

def get_persian_datetime():
    # Define the timezone for Iran
    iran_tz = pytz.timezone('Asia/Tehran')
    
    # Get the current time in UTC and convert it to Iran's timezone
    now = timezone.now().astimezone(iran_tz)
    
    # Convert to Jalali date
    persian_date = JalaliDate(now).strftime('%Y-%m-%d')
    
    # Format time in Iran's timezone
    persian_time = now.strftime('%H:%M:%S')
    
    return persian_date, persian_time

persian_date,persian_time = get_persian_datetime()




class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_id = models.CharField(max_length=255,unique=True)
    transation_code = models.CharField(max_length=255,unique=True)
    date = models.DateField(default=persian_date)
    time = models.TimeField(default=persian_time)


    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} in Order {self.order.order_id}'

