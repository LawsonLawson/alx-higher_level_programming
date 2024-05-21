#!/usr/bin/node
/**
 * Star Wars Movie Characters Fetcher
 *
 * This script makes an HTTP GET request to the Star Wars API (SWAPI) to fetch
 * details about a specific movie, identified by a movie ID provided as a
 * command-line argument. It then fetches and prints the names of all
 * characters appearing in that movie.
 *
 * Usage:
 *   node script_name.js <movie_id>
 *
 * Arguments:
 * <movie_id> (number): The ID of the Star Wars movie to fetch character
 * names for.
 *
 * Example:
 * node script_name.js 1
 *
 * Output:
 * Prints the names of all characters appearing in the specified Star Wars
 * movie.
 */

/* Import the 'request' to handle HTTP requests */
const request = require('request');

/* Construct URL for the Star Wars movie API endpoint using provided id */
const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

/* Make HTTP GET request to fetch details about specified Star Wars movie */
request(movieUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    /* Parse the JSON response to extract list of chars appearing in movie */
    const characters = JSON.parse(body).characters;

    /* Print the names of all characters appearing in the movie */
    printCharacters(characters, 0);
  }
});

/**
 * Recursively prints the names of characters from a given list of character URLs.
 *
 * @param {string[]} characters - An array containing the URLs of characters.
 * @param {number} index - The current index in the characters array.
 */
function printCharacters (characters, index) {
  /* Check if the current index is within the bounds of the characters array */
  if (index < characters.length) {
    /* Make HTTP GET request to fetch details about chars at the current idx */
    request(characters[index], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        /* Parse the JSON response to extract the name of the character */
        const characterName = JSON.parse(body).name;

        /* Print the name of the character */
        console.log(characterName);

        /* Recursively call printCharacters with next idx to print next char */
        printCharacters(characters, index + 1);
      }
    });
  }
}
