
$(document).ready(function(){
    $('.tab a').on('click', function (e) {
        e.preventDefault();

        $(this).parent().addClass('active');
        $(this).parent().siblings().removeClass('active');

        var href = $(this).attr('href');

        $('.forms > form').hide();
        $(href).fadeIn(500);
    });

});


// $(document).ready(() => {
//     $('.loginBtn').click(() => {
//         var name = document.getElementsByName('username').value;
//         var pass = document.getElementsByName('password').value;
        
//         if (name == null || name == "" || pass == null || pass == "" ) {
//             // $("#container").fadeOut(() => {
//             //     $("#empty-container").fadeIn();
//             // });
//             document.getElementById("validate").innerHTML = "Username or Password cannot empty.";
//         }
//     });

//     $('#container input').focus(() => {
//         $('.valid').hide('slow');
//     });
   
//    /* Forgotten Password */
//     $('#forget').click(() => {
//         $("#container").fadeOut(() => {
//             $("#forget-container").fadeIn();
//         });
//     });

//     // close
//     $('.btn-close').click(() => {
//         $("#forget-container").fadeOut(() => {
//             $("#container").fadeIn();
//         });
//     });
// });