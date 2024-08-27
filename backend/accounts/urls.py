from django.urls import path
from .views import SignUpView, LoginView,CurrentUserView,CSRFTokenView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('csrf-token/', CSRFTokenView.as_view(), name='csrf-token'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
]
