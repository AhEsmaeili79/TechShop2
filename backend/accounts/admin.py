from django.contrib import admin
from .models import CustomUser

class AdminView(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email')
    list_display_links = ('id','username','first_name','last_name','email')
    search_fields = ('id','username')

# Register your models here.
admin.site.register(CustomUser)
