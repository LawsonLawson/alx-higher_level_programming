#!/usr/bin/node
/**
 * Star Wars Movie Title Fetcher
 *
 * This script fetches and prints the title of a Star Wars movie from the Star
 * Wars API (SWAPI), based on a movie ID provided as a command-line argument.
 *
 * Usage:
 * node script_name.js <movie_id>
 *
 * Arguments:
 * <movie_id> (number): The ID of the Star Wars movie to fetch the title for.
 *
 * Example:
 * node script_name.js 1
 *
 * Output:
 * Prints the title of the Star Wars movie with the specified ID if the request
 * is successful, or does nothing if an error occurs or the status code is not
 * 200.
 */

/* Import the 'request' module to handle HTTP requests */
const request = require('request');

/* Construct the API URL using the provided movie ID */
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

/* Make an HTTP GET request to the constructed API URL */
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    /* Parse the JSON response and print the movie title */
    const movieTitle = JSON.parse(body).title;
    console.log(movieTitle);
  }
});
