#portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about/', views.about, name="about"),
    path('delete_stock/', views.delete_stock, name="delete_stock"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('delete/<stock_id>/', views.delete, name="delete"),
]



