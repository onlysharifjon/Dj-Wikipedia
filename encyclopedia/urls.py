from django.urls import path
from .views import HomePage, AllPages, CreatePage, DeletePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('all_pages/', AllPages.as_view(), name='all_pages'),
    path('create_page/', CreatePage.as_view(), name='create_page'),
    path('delete_page/<int:pk>/', DeletePage.as_view(), name='delete_page'),
]