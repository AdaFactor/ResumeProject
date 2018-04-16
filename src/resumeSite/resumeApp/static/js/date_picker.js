$(document).ready(function () {
    $("#id_birthday").datepicker({
        dateFormat: "dd/mm/yy",
        changeMonth: true,
        changeYear: true,
        yearRange: "1900:2030"
    });
});