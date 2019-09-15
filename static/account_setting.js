function fill_user_info(f, l, e) {
    document.getElementById("fname").setAttribute("value", f);
    document.getElementById("lname").setAttribute("value", l);
    document.getElementById("user_email").setAttribute("value", e);
}

function submit_enable(){
    let enable = false;
    const u_fname = document.getElementById("fname").value.trim();
    const u_lname = document.getElementById("lname").value.trim();
    const u_curt_psw = document.getElementById("in_current_psw");
    const u_new_psw = document.getElementById("new_psw");
    const u_re_new_psw = document.getElementById("re_new_psw");

    //if first or last name is changed, enable the submit button
    if (u_fname !== s_fname || u_lname !== s_lname){
        enable = true;
    }

    //if the user start typing password, make all three field required and
    //enable the submit button.
    if(u_curt_psw.value.trim() || u_new_psw.value.trim() || u_re_new_psw.value.trim()){
        u_curt_psw.setAttribute("required", "required");
        u_new_psw.setAttribute("required", "required");
        u_re_new_psw.setAttribute("required", "required");
        enable = true;
    }
    else{//Remove the requirement for the passwords.
        u_curt_psw.removeAttribute("required");
        u_new_psw.removeAttribute("required");
        u_re_new_psw.removeAttribute("required");
    }

    //if nothing changed disable the submit button.
    if(u_fname === s_fname && u_lname === s_lname && !(u_curt_psw.value.trim() || u_new_psw.value.trim() || u_re_new_psw.value.trim())){
        enable = false;
    }

    //enable and disable the submit button.
    if(enable){
        document.getElementById("account_setting_submit_button").removeAttribute("disabled");
    }
    else{
        document.getElementById("account_setting_submit_button").setAttribute("disabled", "disabled");
    }
}