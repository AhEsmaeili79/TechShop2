from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from persiantools.jdatetime import JalaliDate
import pytz
from datetime import timedelta

def get_persian_datetime():
    iran_tz = pytz.timezone('Asia/Tehran')
    now = timezone.now().astimezone(iran_tz)
    persian_date = JalaliDate(now).strftime('%Y-%m-%d')
    persian_time = now.strftime('%H:%M:%S')
    return persian_date, persian_time

persian_date, _ = get_persian_datetime()

class CustomUser(AbstractUser):
    Roles = (
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('customer', 'customer'),
    )

    profile_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    phonenumber = models.CharField(max_length=11, null=True)
    date_birth = models.DateField(blank=True, default=persian_date)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    apartment = models.IntegerField(blank=True, null=True)
    role = models.CharField(choices=Roles, default='customer', blank=False)
    zip_code = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    register_date = models.DateField(default=persian_date, blank=False)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'



# token for rest password
class Token(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.created_at + timedelta(minutes=200) < timezone.now()

    def __str__(self):
        return f"{self.user.username} - {self.token}"