from django.urls import path
from .views import UserDetail,signup,login,logout,update_profile

app_name = 'account_api'

urlpatterns = [
    path('<int:pk>/',UserDetail.as_view(),name='detailUser'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('update/<int:id>',update_profile,name='update_profile'),
    path('logout/', logout, name='logout'),
]