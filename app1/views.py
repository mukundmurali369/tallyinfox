from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'base.html')

def load_create_groups(request):
    return render(request,'groups.html')
    
def load_create_ledger(request):
    return render(request,'load_create_ledger.html')

def load_create_select_currency(request):
    return render(request,'load_create_select_currency.html')

def load_create_currency(request):
    return render(request,'load_create_currency.html')

def load_alter_currency(request):
    return render(request,'load_alter_currency.html')

def load_create_vouchertyp(request):
    return render(request,'load_create_vouchertyp.html')
  
def load_create_employee(request):
    return render(request,'load_create_employee.html')

def load_create_empcat(request):
    return render(request,'load_create_empcat.html')

def load_create_empgrp(request):
    return render(request,'load_create_empgrp.html')
    
def load_create_empatnd(request):
    return render(request,'load_create_empatnd.html')

def load_create_unit(request):
    return render(request,'load_create_unit.html')

def load_credit_list(request):
    return render(request,'load_credit_list.html')

def load_multi_ledger_alter(request):
    return render(request,'load_multi_ledger_alter.html')




@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        if len(gname) <= 0:
            return JsonResponse({
                'status': 00
            })

        if len(alia) <= 0:
            alia = None
        else:
            pass

        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        # return redirect('index_view')
        return JsonResponse({
            'status': 1
        })
