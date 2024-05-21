#!/usr/bin/node
/**
 * File Writer Script
 *
 * This script writes a specified string to a file whose path is provided as a
 * command-line argument. If an error occurs while writing to the file, it
 * prints the error message to the console.
 *
 * Usage:
 * node script_name.js <file_path> <string_to_write>
 *
 * Arguments:
 * <file_path> (string): The path to the file where the string will be written.
 * <string_to_write> (string): The string to be written to the file.
 *
 * Example:
 * node script_name.js example.txt "Hello, World!"
 *
 * Output:
 * Writes "Hello, World!" to 'example.txt' if successful,
 * or prints the error message if an error occurs.
 */

/* Import the 'fs' module to handle file system operations */
const fs = require('fs');

/* Read the file path and the string to write from the command-line arguments */
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

/* Write the string to the specified file */
fs.writeFile(filePath, stringToWrite, error => {
  if (error) {
    /* Print the error message if an error occurs */
    console.error(error);
  }
});
