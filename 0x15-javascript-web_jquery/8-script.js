$.get('https://swapi.co/api/films/?format=json', function (titles) {
  $.each(titles['results'], function(data, movies) {
    $("#list_movies").append('<li>' + movies['title'] + '</li>');
  }); }, 'json');
