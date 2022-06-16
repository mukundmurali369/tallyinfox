
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'base.html')

def load_create_groups(request):
    return render(request,'load_create_groups.html')
    
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



def create_ledger(request):
    if request.method == 'POST':
        print('xxxxxxxxxxxxxxxxxxx')
        # Ledger Basic
        Lname = request.POST['Lname']
        Lalias = request.POST['Lalias']
        Lunder = request.POST['Lund']
        Lopening_bal = request.POST['Lopening']
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
        # Provide Banking Details
        provide_banking = request.POST['provide_banking']  # bool

        # Tax_Registration_Details
        Tgst_uin = request.POST['Tgst_uin']
        Treg_typ = request.POST['Treg_typ']
        Tpan_no = request.POST['Tpan_no']
        T_alter_gst = request.POST['T_alter_gst']

        print(
            Lunder,
            Mname,
            Maddress,
            provide_banking,
            Tpan_no

        )

    grp_under_lst = GroupModel.objects.all().order_by('name')
    context = {
        'grp': grp_under_lst,
    }
    return render(request, 'load_create_ledgers.html', context)