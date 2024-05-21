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
 * node script_name.js <movie_id>
 *
 * Arguments:
 * <movie_id> (number): The ID of the Star Wars movie to fetch character names for.
 *
 * Example:
 * node script_name.js 1
 *
 * Output:
 * Prints the names of all characters appearing in the specified Star Wars
 * movie.
 */

/* Import the 'request' module to handle HTTP requests */
const request = require('request');

/* Read the movie ID from the command-line arguments */
const movieId = process.argv[2];

/* Construct the API URL using the provided movie ID */
const movieApiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

/* Make an HTTP GET request to fetch movie details */
request(movieApiUrl, (movieError, movieResponse, movieBody) => {
  if (!movieError && movieResponse.statusCode === 200) {
    /* Parse the JSON response to get movie details */
    const movieDetails = JSON.parse(movieBody);

    /* Get the list of character URLs from the movie details */
    const characterUrls = movieDetails.characters;

    /* Iterate over each character URL */
    for (const characterUrl of characterUrls) {
      /* Make an HTTP GET request to fetch character details */
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (!characterError && characterResponse.statusCode === 200) {
          /* Parse the JSON response to get character details */
          const characterDetails = JSON.parse(characterBody);

          /* Print the character's name */
          console.log(characterDetails.name);
        }
      });
    }
  }
});
