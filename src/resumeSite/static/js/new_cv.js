$(document).ready(function(){
    $("#id_position_other").attr("disabled", "disabled");

    $('#id_position').change(function(){
        if($(this).val() == "ot"){
            $("#id_position_other").removeAttr('disabled');
        } else {
            $("#id_position_other").attr("disabled", "disabled"); 
        }
    });
});
