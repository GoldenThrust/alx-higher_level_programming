$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(req) {
    $('DIV#character').text(req.name);
})