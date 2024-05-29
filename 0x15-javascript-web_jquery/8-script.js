/* global $ */

/**
 * This script fetches data from an API endpoint and inserts all movie titles
 * into the <ul> element with the id "list_movies".
 *
 * The script uses the jQuery method $.get() to send an AJAX GET request to the
 * specified URL ('https://swapi.co/api/films/?format=json').
 * When the request is successful, it retrieves the list of movies from the response data
 * and iterates over each movie, dynamically creating <li> elements for each movie title
 * and appending them to the <ul> element.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Define the URL of the API endpoint */
const url = 'https://swapi.co/api/films/?format=json';

/* Use jQuery $.get() method to fetch data from the API endpoint */
$.get(url, function (data) {
  /* Extract the list of films from the response data */
  const films = data.results;

  /* Iterate over each film and append its title to the <ul> element with id "list_movies" */
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
