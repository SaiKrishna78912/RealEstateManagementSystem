from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='views.index'),
    path('sell/', views.sell, name='sell'),
    path('search-results/', views.search_view, name="search_view"),
    path('buy/', views.buy, name='buy'),
    path('rent/', views.rent, name='rent'),

]
