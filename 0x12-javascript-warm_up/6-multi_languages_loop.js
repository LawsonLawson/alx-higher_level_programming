#!/usr/bin/node
/**
 * A script that prints 3 lines to the console:
 *  “C is fun”
 *  “Python is cool”
 *  “JavaScript is amazing”
 *  This version used loops and arrays of string.
 */
/* Create an array of strings to print */
const stringArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

/* Initialize a counter and set it to 0 */
let i = 0;

/* We loop .... */
while (i < stringArray.length) {
  console.log(stringArray[i]);
  i++;
}
