(function blink(){
    $('.blink_me').fadeOut(1000).fadeIn(1000, blink);
})();


// if no patient found

$(document).ready(function(){
    var verify = $('#check-td').length;
    if(verify == 0){
        $("#no-data").text("No Patient Found!")
    }
})

function validateEmail(email){

regex=  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
return regex


}

function validateAll(){
    var name = $("#name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var age = $("#age").val();


if (name = ''){
    swal("Name field can not be blank!",'error')
    return false;
}
else if (email = ''){
    swal("Email field can not be blank!",'error')
    return false;
}
else if (!(validateEmail(email))){
    swal("Email field can not be blank!",'error')
    $("email").val("");
    return false;
}
else if (phone = ''){
    swal("Phone field can not be blank!",'error')
    return false;
}
else if (age = ''){
    swal("Age field can not be blank!",'error')
    return false;
}
}$("#btn-add").bind("click", validateAll)