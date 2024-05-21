#!/usr/bin/node
/**
 * Star Wars Character Appearance Counter
 *
 * This script makes an HTTP GET request to a specified URL provided as a
 * command-line argument, fetches information about Star Wars films from the
 * Star Wars API (SWAPI), and counts the number of appearances of a specified
 * character in those films.
 *
 * Usage:
 * node script_name.js <api_url>
 *
 * Arguments:
 * <api_url> (string): The URL of the Star Wars API endpoint to fetch
 * information about films.
 *
 * Example:
 * node script_name.js https://swapi.dev/api/films/
 *
 * Output:
 * Prints the number of appearances of the specified character in the Star
 * Wars films fetched from the provided API URL, or prints an error message if
 * an error occurs during the request.
 */

/* Import the 'request' module to handle HTTP requests */
const request = require('request');

/* Read the API URL from the command-line arguments */
const apiUrl = process.argv[2];

/* Define the character whose appearances will be counted */
const characterToCount = { id: 18, name: 'Wedge Antilles' };

/* Make an HTTP GET request to the specified API URL */
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    /* Parse the JSON response */
    body = JSON.parse(body);

    /* Initialize a counter to track the character's appearances */
    let characterAppearanceCount = 0;

    /* Iterate over each film in the results */
    for (const film of body.results) {
      /* Get the list of characters appearing in the current film */
      const charactersInFilm = film.characters;

      /* Iterate over each character in the film's character list */
      for (let i = 0; i < charactersInFilm.length; i++) {
        /* Check if the character's ID is found in the URL of any character in the film */
        if (charactersInFilm[i].endsWith(characterToCount.id + '/')) {
          /* If the character is found, increment the appearance counter */
          characterAppearanceCount++;
        }
      }
    }

    /* Print the total count of appearances of the specified character */
    console.log(characterAppearanceCount);
  } else {
    /* If an error occurs during the request, print the error message */
    console.error(error);
  }
});
