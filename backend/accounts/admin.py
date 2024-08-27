from django.contrib import admin
from .models import CustomUser

class AdminView(admin.ModelAdmin):
    list_display = ('id','username','email')
    list_display_links = ('id','username','email')

# Register your models here.
admin.site.register(CustomUser,AdminView)