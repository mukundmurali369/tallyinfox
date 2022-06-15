
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'base.html')

def load_create_groups(request):
    return render(request,'load_create_groups.html')
    
def load_create_ledgers(request):
    return render(request,'load_create_ledgers.html')

def load_create_select_currency(request):
    return render(request,'load_create_select_currency.html')

def load_create_currency(request):
    return render(request,'load_create_currency.html')

def load_alter_currency(request):
    return render(request,'load_alter_currency.html')

def load_create_vouchertyp(request):
    return render(request,'load_create_vouchertyp.html')

def load_create_empcat(request):
    return render(request,'load_create_empcat.html')

def load_create_empgrp(request):
    return render(request,'load_create_empgrp.html')
    
def load_create_empatnd(request):
    return render(request,'load_create_empatnd.html')