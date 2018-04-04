$(document).ready(function() {
    $('#id_major').change(function() {
        $('#id_branch').val("");

        let major = $('#id_major option:selected').attr('id');
        $('#id_branch option').each(function() {
            let $ele = $(this);
            if(!$ele.hasClass(major))
                $ele.hide();
            else
                $ele.show();
        });
    });
});