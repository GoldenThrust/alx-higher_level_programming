$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(req) {
    $('DIV#hello').text(req.hello);
})