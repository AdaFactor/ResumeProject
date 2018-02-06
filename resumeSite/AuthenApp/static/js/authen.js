$(document).ready(() => {
    // tab login & register
    $('.tabs .tab-links a').on('click', function(e)  {
        var currentAttrValue = $(this).attr('href');
        // Show/Hide Tabs
        $('.tabs ' + currentAttrValue).show().siblings().hide();

        // Change/remove current tab to active
        $(this).parent('li').addClass('active').siblings().removeClass('active');
        e.preventDefault();
    });

    // forget password
    $('#forget').on('click', () => {
        $('#login').hide(() => {
            $('#forgotpassword').show(() => {
                $('.tab-links li').removeClass('active');
            });
        });
    });

    $('#btn-login').on('click', () => {
        var user = $('#username').val();
        var pass = $('#password').val();
        if (user == "" || pass == ""){
            $(".invalidate").html("Username or Password can't leave blank");
            return false;
        }
    });
});