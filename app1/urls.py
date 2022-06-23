from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    
    path('load_create_groups',views.load_create_groups,name='load_create_groups'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('load_create_select_currency',views.load_create_select_currency,name='load_create_select_currency'),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('load_rates_of_exchange',views.load_rates_of_exchange,name='load_rates_of_exchange'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
    path('create_voucher',views.create_voucher,name="create_voucher"),
    path('load_credit_list',views.load_credit_list,name='load_credit_list'),
    path('create_group',views.create_group,name="create_group"),
    path('load_multi_ledger_alter',views.load_multi_ledger_alter,name='load_multi_ledger_alter'),
    path('save_currency_data',views.save_currency_data,name="save_currency_data"),
    

    
    path('load_create_employee',views.load_create_employee,name='load_create_employee'),
    path('save_employee',views.save_employee,name='save_employee'),  
    path('load_create_empcat',views.load_create_empcat,name='load_create_empcat'),
    path('save_empcat',views.save_empcat,name='save_empcat'),
    path('save_empgrp',views.save_empgrp,name='save_empgrp'),
    path('save_empattend',views.save_empattend,name='save_empattend'),  
    path('load_create_empgrp',views.load_create_empgrp,name='load_create_empgrp'),
    path('load_create_empatnd',views.load_create_empatnd,name='load_create_empatnd'),  
    path('load_create_unit',views.load_create_unit,name='load_create_unit'),  
]