from decimal import Decimal
import email
from locale import currency
from optparse import make_option

from unicodedata import decimal
from django.db import models

# Create your models here.
class GroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    gp_behaves_like_sub_ledger = models.BooleanField(default=False)
    nett_debit_credit_bal_reporting = models.BooleanField(default=False)
    used_for_calculation = models.BooleanField(default=False)
    method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
        return self.name
    
class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)
    flag= models.CharField(max_length=225,default=0)

class CreateEmployeeCategory(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    allocate_revenue=models.CharField(max_length=225)
    allocate_nonrevenue=models.CharField(max_length=225)

class CreateEmployeegroup(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    define_salary=models.CharField(max_length=225)

class CreateAttendence(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    typee =models.CharField(max_length=225)



class VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)
   


class CurrencyAlter(models.Model):
    cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
    slno = models.CharField(max_length=225)
    currencys = models.CharField(max_length=225)
    stdrate =models.CharField(max_length=225)
    lastvrate =models.CharField(max_length=225)
    specirate =models.CharField(max_length=225)
    lastvrate2 =models.CharField(max_length=225)
    specirate2 =models.CharField(max_length=225)

class Employee(models.Model):

    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    emailid =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)



class CompanyModel(models.Model):
    cname = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)
    telephone = models.CharField(max_length=225)
    mobile = models.CharField(max_length=225)
    fax = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.CharField(max_length=225)
    is_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    #
    currency_symbol = models.CharField(max_length=225, default='₹')
    currency_formal_name = models.CharField(max_length=225, default='INR')
    #
    financial_year = models.DateField()
    books_beginning_from = models.DateField()

    def __str__(self):
        return self.cname
        
class LedgerModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_name = models.CharField(max_length=225)
    ledger_alias = models.CharField(max_length=225)

    group = models.ForeignKey(
        GroupModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_opening_bal = models.CharField(max_length=225)
    ledger_type = models.CharField(max_length=225)
    type_of_duty = models.CharField(max_length=225)
    percent_of_calculation = models.CharField(max_length=225)
    maintain_bal_bill = models.CharField(max_length=225)
    credit_days_during_voucher_entry = models.CharField(max_length=225)
    default_cr_peroid = models.CharField(max_length=225)
    provide_banking_details = models.BooleanField()

    def __str__(self):
        return self.ledger_name


class BankingDetails(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225)
    holder_name = models.CharField(max_length=225)
    ac_number = models.CharField(max_length=225)
    ifsc = models.CharField(max_length=225)
    swift_code = models.CharField(max_length=225)
    bank_name = models.CharField(max_length=225)
    branch_name = models.CharField(max_length=225)
    alter_chk_bks = models.BooleanField()
    enbl_chk_printing = models.BooleanField()


class MailingAddressModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)


class TaxRegisterModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225)
    register_type = models.CharField(max_length=225)
    pan_no = models.CharField(max_length=225)
    alter_gst_details = models.BooleanField()


class LedgerSatutoryModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225)
    gst_applicable = models.CharField(max_length=225)
    type_of_supply = models.CharField(max_length=225)
