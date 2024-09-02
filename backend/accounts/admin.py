from django.contrib import admin

# Register your models here.
from .models import CustomUser

class adminView(admin.ModelAdmin):
    list_display=('id','username','first_name')
    list_display_links= ('id','username','first_name')

admin.site.register(CustomUser,adminView)