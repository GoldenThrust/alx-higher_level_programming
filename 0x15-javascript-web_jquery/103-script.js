$('document').ready(function () {
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').focus(function (e) {
        $(this).keydown(function (e) {
            if (e.key === 'Enter') {
                translate();
            }
        });
    });
});

function translate() {
    $.get('https://www.fourtonfish.com/hellosalut/?' + $.param({ lang: $('INPUT#language_code').val() }), function (req) {
        $('DIV#hello').html(req.hello);
    });
}