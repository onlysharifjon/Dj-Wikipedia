from django.urls import path
from .views import HomePage, AllPages, CreatePage, DeletePage, EditPage, DetailPage, RandomPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('all_pages/', AllPages.as_view(), name='all_pages'),
    path('create_page/', CreatePage.as_view(), name='create_page'),
    path('random_page/', RandomPage.as_view(), name='random_page'),
    path('delete_page/<int:pk>/', DeletePage.as_view(), name='delete_page'),
    path('edit_page/<int:pk>/', EditPage.as_view(), name='edit_page'),
    path('detail_page/<slug:slug>/', DetailPage.as_view(), name='detail_page'),
    path('search_page/', DetailPage.as_view(), name='search_page'),
]