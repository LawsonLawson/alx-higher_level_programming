#!/usr/bin/node
/**
 * Completed Task Counter Script
 *
 * This script makes an HTTP GET request to a specified URL provided as a
 * command-line argument, fetches a list of tasks, and counts the number of
 * completed tasks per user.
 *
 * Usage:
 * node script_name.js <api_url>
 *
 * Arguments:
 * <api_url> (string): The URL of the API endpoint to fetch the list of tasks.
 *
 * Example:
 * node script_name.js https://example.com/api/tasks
 *
 * Output:
 * Prints a dictionary containing the number of completed tasks per user ID.
 */

/* Import the 'request' module to handle HTTP requests */
const request = require('request');

/* Read the API URL from the command-line arguments */
const apiUrl = process.argv[2];

/* Make an HTTP GET request to the specified API URL */
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    /* Initialize empty dict to store the count of completed tasks per user */
    const completedTasksCountByUser = {};

    /* Parse the JSON response */
    body = JSON.parse(body);

    /* Iterate over each task in the response */
    for (const task of body) {
      /* Check if the task is completed */
      if (task.completed === true) {
        /* Increment the completed tasks count for the user */
        if (completedTasksCountByUser[task.userId]) {
          completedTasksCountByUser[task.userId]++;
        } else {
          completedTasksCountByUser[task.userId] = 1;
        }
      }
    }

    /* Print the dictionary containing the count of completed tasks per user */
    console.log(completedTasksCountByUser);
  }
});
