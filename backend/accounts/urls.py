from django.urls import path
from .views import UserDetail,signup,login,logout,update_profile

app_name = 'account_api'

urlpatterns = [
    path('user/', UserDetail, name='user_profile'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('user/update/', update_profile, name='update_profile'),
    path('logout/', logout, name='logout'),
]