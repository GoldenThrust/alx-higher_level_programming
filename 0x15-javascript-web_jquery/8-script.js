$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
    if (status === 'success') {
        $.each(data.results, function(index, film) {
            $('ul#list_movies').append('<li>' + film.title + '</li>');
        });
    }
});
