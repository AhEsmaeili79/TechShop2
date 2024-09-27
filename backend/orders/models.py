from django.db import models
from accounts.models import CustomUser
from products.models import Product

# Create your models here.

from django.utils import timezone
from persiantools.jdatetime import JalaliDate
import pytz


def get_persian_datetime():
    # Define the timezone for Iran
    iran_tz = pytz.timezone("Asia/Tehran")

    # Get the current time in UTC and convert it to Iran's timezone
    now = timezone.now().astimezone(iran_tz)

    # Convert to Jalali date
    persian_date = JalaliDate(now).strftime("%Y-%m-%d")

    # Format time in Iran's timezone
    persian_time = now.strftime("%H:%M:%S")

    return persian_date, persian_time


persian_date, persian_time = get_persian_datetime()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    transation_code = models.CharField(max_length=255, unique=True)
    date = models.DateField(default=persian_date)
    time = models.TimeField(default=persian_time)

    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} in Order {self.order.order_id}"
