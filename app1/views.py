from multiprocessing import context
from sys import flags
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

def save_employee(request):

    if request.method == 'POST':

        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['underr']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        
        mdl_obj = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            emailid = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,


        )

        mdl_obj.save()
        return render(request,'load_create_employee.html')



    




def load_create_empcat(request):
    return render(request,'load_create_empcat.html')

def load_create_empgrp(request):
    return render(request,'load_create_empgrp.html')
    
def load_create_empatnd(request):
    grp = CreateAttendence.objects.all()
    context={'grp':grp,}
    return render(request,'load_create_empatnd.html',context)

def load_create_unit(request):
    return render(request,'load_create_unit.html')

def load_credit_list(request):
    return render(request,'load_credit_list.html')

def load_multi_ledger_alter(request):
    return render(request,'load_multi_ledger_alter.html')

def load_rates_of_exchange(request):
    grp = CreateCurrency.objects.all()
    grp2 = CreateCurrency.objects.all().filter(flag="0")
    obj = CurrencyAlter.objects.all()
    context={'grp':grp ,'obj':obj,'grp2':grp2}
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

    
def save_currency_data(request):
    if request.method == 'POST':
        sl = request.POST['slno']
        cname = request.POST['curname']
        stdr = request.POST['stdr']
        lvr = request.POST['lvr']
        sr = request.POST['sr']
        lvr2 = request.POST['lvr2']
        sr2 = request.POST['sr2']
        
        obj = CurrencyAlter(
            slno = sl,
            currencys= cname,
            stdrate = stdr,
            lastvrate = lvr,
            specirate = sr,
            lastvrate2 = lvr2,
            specirate2 = sr2,
            
            
           
        )
        
        obj.save()
        grp = CreateCurrency.objects.all()
        obj1 = CurrencyAlter.objects.all()
        context = {'grp':grp ,'obj':obj1}
        return redirect('load_rates_of_exchange',context)


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


def save_empgrp(request):
    if request.method == 'POST':
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['underr']
        sal = request.POST['sal']
        
        mdl_obj = CreateEmployeegroup(
            name =namee,
            alias=aliass,
            under=underr,
            define_salary=sal,
           
        )
        mdl_obj.save()
        return redirect('load_create_empcat')


def save_empattend(request):
    if request.method == 'POST':
        namee = request.POST['name']
        aliass = request.POST['aliass']
        underr = request.POST['under']
        type = request.POST['type']
        
        mdl_obj = CreateAttendence(
            name =namee,
            alias=aliass,
            under=underr,
            typee=type,
           
        )
        mdl_obj.save()
        return redirect('load_create_empatnd')





def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        # useadv= request.POST['useadvc']
        # prvtdp= request.POST['prvtdp']

        # if meth_vou_num == "auto":
        #     useadv= request.POST['useadvc']
        #     prvtdp ="Null"
        # elif meth_vou_num == "manu":
        #     prvtdp= request.POST['prvtdp']
        #     useadv ="Null"
        # elif meth_vou_num == "overd":
        #     prvtdp= request.POST['prvtdp']
        #     useadv = request.POST['useadvc']
        # elif meth_vou_num == "multi":
        #     useadv= request.POST['useadvc']
        #     prvtdp ="Null"
        # else:
        #     prvtdp="Null"
        #     useadv="Null"


        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool
        
        mdl = VoucherModels(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        mdl.save()
        return redirect('load_create_vouchertyp')

    return render(request, 'load_create_vouchertyp')



def create_ledger(request):
    if request.method == 'POST':

        # Ledger Basic
        Lname = request.POST['Lname']
        Lalias = request.POST['Lalias']
        Lunder = request.POST['Lund']
        try:
            mdl = GroupModel.objects.get(name=Lunder)

            fl = mdl
            print('IN name')
        except:

            try:
                mdl = GroupModel.objects.get(alias=Lunder)
                print('in ALIAS')
                fl = mdl
            except:
                print("NOT found")

        Lopening_bal = request.POST['Lopening']
        typ_of_ledg = request.POST['typ_of_ledg']
        typ_of_duty = request.POST['typ_of_duty']
        percet_of_calc = request.POST['percet_of_calc']
        main_balance_bill_ = request.POST['main_balance_bill_']  # bool
        chk_credit_days = request.POST['chk_credit_days']  # bool
        def_cr_period = request.POST['def_cr_period']
        # Provide Banking Details
        provide_banking = request.POST['provide_banking']  # bool

        # Banking_details
        B_od_limit = request.POST['B_od_limit']
        B_ac_holder_name = request.POST['B_ac_name']
        B_ac_no = request.POST['B_ac_no']
        B_ifsc = request.POST['B_ac_ifsc']
        B_swift_code = request.POST['B_ac_swift']
        B_name = request.POST['B_name']
        B_branch = request.POST['B_branch']
        '''bank Configuration'''
        B_alter_chq_bks = request.POST['B_alter_chq_bks']  # bool
        B_name_enbl_chq_prtg = request.POST['B_name_enbl_chq_prtg']  # bool

        # Mailing_details
        Mname = request.POST['Mname']
        Maddress = request.POST['Maddress']
        Mstate = request.POST['Mstate']
        Mcountry = request.POST['Mcountry']
        Mpincode = request.POST['Mpincode']

        # Tax_Registration_Details
        Tgst_uin = request.POST['Tgst_uin']
        Treg_typ = request.POST['Treg_typ']
        Tpan_no = request.POST['Tpan_no']
        T_alter_gst = request.POST['T_alter_gst']

        # Satutory Details
        assemble_calc = request.POST['assemble_value']
        is_gst_applicable = request.POST['is_gst_applicable']
        typ_of_supply = request.POST['typ_of_supply']

        # -------------------------#
        sec = CompanyModel.objects.get(id=request.session["scid"])
        Lmdl = LedgerModel(
            cid=sec,
            ledger_name=Lname,
            ledger_alias=Lalias,
            group=fl,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            type_of_duty=typ_of_duty,
            percent_of_calculation=percet_of_calc,
            maintain_bal_bill=main_balance_bill_,
            credit_days_during_voucher_entry=chk_credit_days,
            default_cr_peroid=def_cr_period,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = BankingDetails(
            cid=sec,
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,
        )
        Bmdl.save()
        M_mdl = MailingAddressModel(
            cid=sec,
            ledger_id=idd,
            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = TaxRegisterModel(
            cid=sec,
            ledger_id=idd,
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = LedgerSatutoryModel(
            cid=sec,
            ledger_id=idd,
            assessable_calculation=assemble_calc,
            gst_applicable=is_gst_applicable,
            type_of_supply=typ_of_supply,


        )
        LS_mdl.save()
        return redirect('index_view')

    grp_under_lst = GroupModel.objects.all().order_by('name')
  
    context = {
        'grp': grp_under_lst,
        
    }
    return render(request, 'create_ledger.html', context)
