$.get('https://swapi.co/api/people/5/?format=json', function(characters) {
  $('DIV#character').text(characters.name); }, 'json');
