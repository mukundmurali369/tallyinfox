from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('load_create_groups',views.load_create_groups,name='load_create_groups'),
    path('load_create_ledgers',views.load_create_ledgers,name='load_create_ledgers'),
    path('load_create_select_currency',views.load_create_select_currency,name='load_create_select_currency'),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
]