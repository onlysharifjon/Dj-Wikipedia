from django.urls import path
from .views import HomePage, AllPages

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('all_pages/', AllPages.as_view(), name='all_pages'),
]