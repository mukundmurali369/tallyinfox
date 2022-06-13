from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('load_create_groups',views.load_create_groups,name='load_create_groups'),
    path('load_create_ledgers',views.load_create_ledgers,name='load_create_ledgers'),
]