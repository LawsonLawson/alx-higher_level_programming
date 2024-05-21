#!/usr/bin/node
/**
 * File Downloader Script
 *
 * This script downloads a file from a specified URL provided as the first command-line argument,
 * and saves it to a specified file path provided as the second command-line argument.
 *
 * Usage:
 *   node script_name.js <api_url> <file_path>
 *
 * Arguments:
 *   <api_url> (string): The URL of the file to download.
 *   <file_path> (string): The path where the downloaded file will be saved.
 *
 * Example:
 *   node script_name.js https://example.com/file.txt ./downloaded_file.txt
 *
 * Output:
 *   Downloads the file from the specified URL and saves it to the specified file path.
 */

/* Import the 'request' module to handle HTTP request */
const request = require('request');

/* Import the 'fs' module to handle file system operations */
const fs = require('fs');

/* Read the API URL and file path from the command-line arguments */
const fileUrl = process.argv[2];
const destinationFilePath = process.argv[3];

/* Make HTTP GET request to download file & pipe response to writable stream */
request(fileUrl).pipe(fs.createWriteStream(destinationFilePath));
