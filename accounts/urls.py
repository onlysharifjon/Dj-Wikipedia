from django.urls import path
from .views import RegisterUser, LoginUser, CustomLogoutView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
