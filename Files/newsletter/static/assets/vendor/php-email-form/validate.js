function validate(){

    let f = false;
    var check_fname = false;
    var check_lname = false;
    var check_email = false;
    var check_pwd = false;
    var check_dept = false;

    //validate fname
    let fname = $("#form_fname").val();
    if (fname == '' || fname == undefined) {
        $("#fname_error_message").html('First Name is required.');
        check_fname = false;
    } 
    else {
        $("#fname_error_message").hide();
        check_fname = true;
    } 
    
    //validate lname
    let lname = $("#form_lname").val();
    if (lname == '' || lname == undefined) {
        $("#lname_error_message").html('Last Name is required.');
        check_lname = false;
    } 
    else {
        $("#lname_error_message").hide();
        check_lname = true;
    } 

    //validate email
    let email = $("#form_email").val();
    let exp =  /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email == '' || email == undefined) {
        $("#email_error_message").html('Email is required.');
        check_email = false;
    }
    else if (exp.test(email) == false) {
        $("#email_error_message").html('Invalid email.');
        check_email = false;
    }
    else {
        $("#email_error_message").hide();
        check_email = true;
    }

    //validate password
    let pwd = $("#form_pwd").val();
    if (pwd == '' || pwd == undefined) {
        $("#pwd_error_message").html('Password is required.');
        check_pwd = false;
    }
    else {
        check_pwd = true;
    }

    let con_pwd = $("#form_con_pwd").val();
    if (con_pwd == '' || con_pwd == undefined) {
        $("#conpwd_error_message").html('Confirm your password.');
        check_pwd = false;
    }
    else {
        $("#pwd_error_message").hide();
        $("#conpwd_error_message").hide();
        check_pwd = true;
    }

    if (pwd !== con_pwd) {
        $("#pwd_error_message").html('Passwords do not match.');
        $("#conpwd_error_message").html('Passwords do not match.');
        $("#pwd_error_message").show();
        $("#conpwd_error_message").show();
        check_pwd = false;
    }
    else {
        check_pwd = true;
    }

    //validate department
    // let dept = $("#form_dept").val();
    // if (dept == 'Department') {
    //     $("#dept_error_message").html('Please select your department.');
    //     check_dept = false;
    // } 
    // else {
    //     $("#dept_error_message").hide();
    //     check_dept = true;
    // }

    // if (check_fname === true && check_lname === true && check_email === true && check_pwd === true && check_dept === true) {
    //     f = true;
    // }
    // else {
    //     f = false;
    // }

    if (check_fname === true && check_lname === true && check_email === true && check_pwd === true) {
        f = true;
    }
    else {
        f = false;
    }
    return f;
 }

function validateSignIn(){

    let f = false;
    var check_email = false;
    var check_pwd = false;
   
    //validate email
    let email = $("#form_email").val();
    let exp =  /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email == '' || email == undefined) {
        $("#email_error_message").html('Email is required.');
        check_email = false;
    }
    else if (exp.test(email) == false) {
        $("#email_error_message").html('Invalid email.');
        check_email = false;
    }
    else {
        $("#email_error_message").hide();
        check_email = true;
    }

    let pwd = $("#form_pwd").val();
    if (pwd == '' || pwd == undefined) {
        $("#pwd_error_message").html('Password is required.<br>');
        check_pwd = false;
        }
    else {
        check_pwd = true;
    }

    if (check_email === true && check_pwd === true) {
        f = true;
    }
    else {
        f = false;
    }
    return f;
}