function h() {
    $('#acc_allocation').hide()
    $('#adtl_cost_for_purch').hide()
    $('#pr').hide()
    $('#opt_default').show()
    $('#manfact_jou').hide()
    //
    $('#print_voucher').hide()
    $('#def_jur').hide()
    $('#def_title').hide()
    $('#print_formal').hide()
    $('#se_alter').hide()




}
function typ_of_voucher(val) {
    console.log(val)
    if (val == 'contra') {
        $('#print_voucher').show()
        $('#acc_allocation').show()
        $('#pr').show()
    } else if (val == 'Debit Note') {
        $('#def_title').show()
        $('#print_voucher').show()
        $('#adtl_cost_for_purch').show()
        $('#acc_allocation').show()
    } else if (val == 'Delivery Note') {
        $('#print_voucher').show()
        $('#acc_allocation').show()
        $('#def_jur').show()
        $('#def_title').show()
    } else if (val == 'Attendence') {
        $('#print_voucher').show()
        $('#pr').show()
    } else if (val == 'Credit Note') {
        $('#print_voucher').show()
        $('#pr').show()
        $('#print_voucher').show()
        $('#def_jur').show()
        $('#def_title').show()

    } else if (val == 'Journal') {
        $('#print_voucher').show()
        $('#acc_allocation').show()
        $('#pr').show()
    } else if (val == 'Memorandum') {
        $('#print_voucher').show()
        $('#adtl_cost_for_purch').show()
        $('#pr').show()
        $('#opt_default').hide()

    } else if (val == 'Payment') {
        $('#print_voucher').show()
        $('#adtl_cost_for_purch').show()
        $('#pr').show()
        $('#acc_allocation').show()
    } else if (val == 'Payroll') {
        $('#print_voucher').show()
        $('#pr').show()
    } else if (val == 'Physical Stock') {
        $('#print_voucher').show()
        $('#opt_default').hide()
        $('#adtl_cost_for_purch').show()

    } else if (val == 'Purchase') {
        $('#print_voucher').show()
        $('#adtl_cost_for_purch').show()
        $('#pr').show()
        $('#acc_allocation').show()
    } else if (val == 'Purchase Order') {
        $('#def_jur').show()
        $('#print_voucher').show()
        $('#acc_allocation').show()

    } else if (val == 'Receipt') {
        $('#print_formal').show()
        $('#print_voucher').show()
        $('#pr').show()
        $('#acc_allocation').show()

    } else if (val == 'Receipt Note') {
        $('#print_voucher').show()

        $('#acc_allocation').show()

    } else if (val == 'Rejection Out') {
        $('#print_voucher').show()
        $('#adtl_cost_for_purch').show()

    } else if (val == 'Reversing Journal') {
        $('#print_voucher').show()
        $('#opt_default').hide()
        $('#adtl_cost_for_purch').show()
        $('#pr').show()
    } else if (val == 'Sales') {
        $('#se_alter').show()
        $('#def_jur').show()
        $('#def_title').show()
        $('#print_voucher').show()
        $('#acc_allocation').show()
        $('#pr').show()
    } else if (val == 'Sales Order') {
        $('#se_alter').show()
        $('#print_voucher').show()
        $('#acc_allocation').show()
    } else if (val == 'Stock Journal') {
        $('#print_voucher').show()
        $('#manfact_jou').show()
    } else if (val == 'Job Work in Order') {
        $('#def_title').show()
        $('#print_voucher').show()
    } else if (val == 'Job Work Out Order') {
        $('#def_jur').show()
        $('#def_title').show()
        $('#print_voucher').show()
    } else if (val == 'Material In') {
        $('#print_voucher').show()
    } else if (val == 'Material Out') {
        $('#def_jur').show()
        $('#print_voucher').show()
    } else if (val == 'Rejection In') {
        $('#print_voucher').show()
    }

    else {
        //else if(val==''){}
    }
}   