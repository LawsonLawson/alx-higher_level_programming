#!/usr/bin/node
/**
 * File Reader Script
 *
 * This script reads the content of a file specified by a command-line argument
 * and prints the content to the console.
 *
 * Usage:
 * node script_name.js <file_path>
 *
 * Arguments:
 * <file_path> (string): The path to the file to be read.
 *
 * Example:
 * node script_name.js example.txt
 *
 * Output:
 * The content of the file is printed to the console. If there is an error,
 * the error message is printed instead.
 */

/* Import the file system module to handle file operations */
const fs = require('fs');

/* Check if the script receives the correct number of arguments */
if (process.argv.length !== 3) {
  console.log('Usage: node script_name.js <file_path>');
  process.exit(1);
}

/* Get the file path from the command-line arguments */
const filePath = process.argv[2];

/* Read the content of the file specified by the file path */
fs.readFile(filePath, 'utf8', function (err, content) {
  if (err) {
    /* If there is an error reading the file, print the error message */
    console.log(err);
  } else {
    /* If the file is read successfully, print its content */
    console.log(content);
  }
});
