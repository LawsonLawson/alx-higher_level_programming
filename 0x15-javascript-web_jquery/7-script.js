/* global $ */

/**
 * This script fetches data from an API endpoint and replaces the name of
 * the character in the <div> element with the id "character" with the fetched name.
 *
 * The script uses the jQuery method $.get() to send an AJAX GET request to the
 * specified URL ('https://swapi.co/api/people/5/?format=json').
 * When the request is successful, the name of the character returned by the API
 * is extracted from the response data and set as the text content of the <div> element.
 *
 * Note:
 * - This script assumes that jQuery is loaded and available in the HTML document.
 * - It is recommended to ensure that this script is executed after the DOM is fully loaded.
 * - This script is intended to be semistandard compliant with the flag --global $.
 */

/* Define the URL of the API endpoint */
const url = 'https://swapi.co/api/people/5/?format=json';

/* Use jQuery $.get() method to fetch data from the API endpoint */
$.get(url, function (data, stat) {
  /* Extract the name of the character from the response data */
  const characterName = data.name;

  /* Update the text content of the <div> element with id "character" to the fetched name */
  $('div#character').text(characterName);
});
