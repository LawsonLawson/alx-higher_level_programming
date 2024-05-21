#!/usr/bin/node
/**
 * HTTP Status Code Checker Script
 *
 * This script makes an HTTP GET request to a specified URL provided as a
 * command-line argument and prints the response status code to the console.
 * If an error occurs during the request, it prints the error message to the
 * console.
 *
 * Usage:
 * node script_name.js <url>
 *
 * Arguments:
 * <url> (string): The URL to which the HTTP GET request will be made.
 *
 * Example:
 * node script_name.js https://example.com
 *
 * Output:
 * Prints the HTTP status code of the response, or prints the error message if
 * an error occurs.
 */

/* Import the 'request' module to handle HTTP requests */
const request = require('request');

/* Read the URL from the command-line arguments */
const url = process.argv[2];

/* Make an HTTP GET request to the specified URL */
request(url, (error, response) => {
  if (error) {
    /* Print the error message if an error occurs */
    console.error(error);
  } else {
    /* Print the HTTP status code of the response */
    console.log('code: ' + response.statusCode);
  }
});
