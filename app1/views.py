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

def load_rates_of_exchange(request):
    obj=CreateCurrency.objects.all()
    context={'grp': obj}
    return render(request,'load_rates_of_exchange.html',context)




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


def create_currency(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        fname = request.POST['fname']
        if len(symbol) <= 0:
            print('XX')
            return JsonResponse({
                'status': 00
            })
        elif len(fname) <= 0:
            print('XXX')
            return JsonResponse({
                'status': 00
            })
        else:
            pass

        iso_code = request.POST['iso_code']
        n_deci_placs = request.POST['n_deci_placs']
        smt_millon = request.POST['smt_millon']
        symbol_to_amount = request.POST['symbol_to_amount']
        space_bt_sy = request.POST['space_bt_sy']
        amount_after_decimal = request.POST['amount_after_decimal']
        amount_in_words = request.POST['amount_in_words']

        mdl_obj = CreateCurrency(
            symbol=symbol,
            formal_name=fname,
            ISO_code=iso_code,
            decimal_places=n_deci_placs,
            show_in_millions=smt_millon,
            suffix_to_amount=symbol_to_amount,
            space_symbol_amount=space_bt_sy,
            word_after_decimal=amount_after_decimal,
            decimal_no_in_words=amount_in_words,
        )
        mdl_obj.save()
        return redirect('load_create_currency')


def save_empcat(request):
    if request.method == 'POST':
        namee = request.POST['name']
        aliass = request.POST['alias']
        rev = request.POST['allocaterev']
        nonrev = request.POST['allocatenonrev']
        
        mdl_obj = CreateEmployeeCategory(
            name =namee,
            alias=aliass,
            allocate_revenue=rev,
            allocate_nonrevenue=nonrev,
           
        )
        mdl_obj.save()
        return redirect('load_create_empcat')



def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        enbl_def_accout_alloc = request.POST['enbl_def_accout_alloc']  # bool
        track_addi_coast = request.POST['track_addi_coast']  # bool
        # bool
        use_as_manfacturing_journal = request.POST['use_as_manfacturing_journal']
        #
        print_vou_aft_save = request.POST['print_vou_aft_save']  # b
        print_formal_recept = request.POST['print_formal_recept']  # b
        def_juri = request.POST['def_juri']
        default_title = request.POST['default_title']
        alte_declaration = request.POST['alte_declaration']  # b

        mdl = VoucherModel(
            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            enable_default_ac_allocation=enbl_def_accout_alloc,
            track_additional_cost_purchase=track_addi_coast,
            use_as_manf_journal=use_as_manfacturing_journal,
            print_voucher_af_save=print_vou_aft_save,
            print_formal_recept=print_formal_recept,
            default_juridiction=def_juri,
            default_title=default_title,
            alter_decalaration=alte_declaration,

        )
        mdl.save()
        return redirect('base.html')

    context = {

    }
    return render(request, 'load_create_vouchertyp', context)