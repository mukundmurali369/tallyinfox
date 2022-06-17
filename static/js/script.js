
function h() {
    $('#OD').hide()
    $('#provide_banking').hide()
    $('#bank_ac_details')
    $('#all').hide()
    $('#tax_resgistration_details')
    $('#tax_uin').hide()
    $('#tax_reg_typ').hide()
    $('#tax_pan').hide()
    $('#tax_alter_gst').hide()
    $('#tax_reg_typ').hide()
    $('#tax_pan').hide()
    $('#tax_alter_gst').hide()
    $('#provide_banking').hide()
    $('#Satutory_details').hide()
    $('#mail_state').hide()
    $('#mail_country').hide()
    $('#mail_pincode').hide()
    $('#mail_name').hide()

    $('#provide_banking').hide()

    $('#bank_ac_details').hide()
    // 
    $('#assemble_satu').hide()
    $('#is_gst_applicable').hide()
    $('#typ_of_suply').hide()
    // 
    $('#typ_of_ledg').hide()
    $('#typ_of_duty').hide()
    $('#percet_of_calc').hide()
    $('#main_balance_bill_').hide()
    $('#def_cr_period').hide()
    $('#chk_credit_days').hide()



};
function undertaker(a, b) {
    $('#all').show()
    var val = a;
    var vin = b;
    console.log(val, vin)

    showforms(vin);
    function showforms(vin) {


        if (vin == 'Bank Accounts' | vin == 'Bank OD A/c' | vin == 'Bank OCC A/c') {
            $('#tax_uin').show()

            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()


            if (vin == 'Bank OD A/c' | vin == 'Bank OCC A/c') {
                $('#OD').show()
                $('#tax_uin').show()
                $('#bank_ac_details').show()
                $('#mail_name').show()
                $('#mail_address').show()
                $('#mail_state').show()
                $('#mail_country').show()
                $('#mail_pincode').show()
                $('#mail_state').show()
                $('#mail_country').show()
                $('#mail_pincode').show()
            }
            else {
                $('#OD').hide()
                $('#bank_ac_details').show()

            }

        } else if (vin == 'Branch/Division') {

            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#provide_banking').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()





        } else if (vin == 'Capital Accounts') {

            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#provide_banking').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#mail_name').show()
            $('#mail_address').show()


        }
        else if (vin == 'Cash-in-Hand') {
            $('#provide_banking').show()
            $('#mail_address').show()
            $('#tax_pan').show()
            $('#mail_state').hide()
            $('#mail_name').show()



        } else if (vin == 'Current Assets') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#Satutory_details').show()
            $('#assemble_satu').show()


        } else if (vin == 'Current Liabilities') {

            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
        } else if (vin == 'Deposits(Asset)') {

            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()

        } else if (vin == 'Direct Expenses' | vin == 'Expenses(Direct)') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#Satutory_details').show()
            $('#typ_of_ledg').show()
            $('#tax_pan').show()
            $('#assemble_satu').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()


        } else if (vin == 'Direct Income' | vin == 'Income(Direct)') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#Satutory_details').show()
            $('#typ_of_ledg').show()
            $('#tax_pan').show()
            $('#assemble_satu').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()
        } else if (vin == 'Duties & Taxes') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#typ_of_duty').show()
            $('#percet_of_calc').show()
            $('#tax_pan').show()
            $('#provide_banking').show()
        } else if (vin == 'Fixed Assets') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#Satutory_details').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()

        } else if (vin == 'Indirect Expenses' | vin == 'Expenses(Indirect)') {
            $('#typ_of_ledg').show()
            $('#Satutory_details').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_pan').show()

        } else if (vin == 'Indirect Income' | vin == 'Income(indirect)') {

            $('#typ_of_ledg').show()
            $('#Satutory_details').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_pan').show()

        } else if (vin == 'Investments') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_pan').show()


        } else if (vin == 'Loans & Advances (Asset)') {

            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()

        } else if (vin == 'Loans (Liability)') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#Satutory_details').show()
            $('#assemble_satu').show()
        } else if (vin == 'Misc.Exoence(ASSET)') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()


        } else if (vin == 'Provisions') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()


        } else if (vin == 'Purchase Accounts') {
            $('#typ_of_ledg').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()
            $('#Satutory_details').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()


        } else if (vin == 'Reserves & Surplus' | vin == 'Reataine Earnings') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()

        } else if (vin == 'Sales Accounts') {
            $('#typ_of_ledg').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()
            $('#Satutory_details').show()
            $('#is_gst_applicable').show()
            $('#typ_of_suply').show()


        } else if (vin == 'Secured Loans') {
            $('#Satutory_details').show()
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#assemble_satu').show()


        } else if (vin == 'Stock-in-Hand') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()


        } else if (vin == 'Sundry Creditors') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#main_balance_bill_').show()
            $('#def_cr_period').show()
            $('#chk_credit_days').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()


        } else if (vin == 'Sundry Debtors') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#main_balance_bill_').show()
            $('#def_cr_period').show()
            $('#chk_credit_days').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
        }
        else if (vin == 'Suspence A/c') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#provide_banking').show()
            $('#tax_pan').show()
        }
        else if (vin == 'Unsecured Loans') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#Satutory_details').show()
            $('#assemble_satu').show()

        }


        else {
            $('#all').hide()
            

        }
    }


    showunder(val);
    function showunder(val) {
        if (val == 'primary') {
            under;
            document.getElementById('und').innerHTML = ''
        }
        else {
            let under = val
            document.getElementById('und').innerHTML = '(' + under + ')'
        }
    }
}