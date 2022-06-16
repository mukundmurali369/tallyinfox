from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('load_create_groups',views.load_create_groups,name='load_create_groups'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('load_create_select_currency',views.load_create_select_currency,name='load_create_select_currency'),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),

    
    path('load_create_employee',views.load_create_employee,name='load_create_employee'), 
    path('load_create_empcat',views.load_create_empcat,name='load_create_empcat'), 
    path('load_create_empgrp',views.load_create_empgrp,name='load_create_empgrp'),
    path('load_create_empatnd',views.load_create_empatnd,name='load_create_empatnd'),  
    path('load_create_unit',views.load_create_unit,name='load_create_unit'),  
]