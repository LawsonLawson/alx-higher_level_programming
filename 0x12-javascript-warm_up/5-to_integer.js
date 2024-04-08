#!/usr/bin/node

/**
 * A script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */
/* Argument to check */
const argument = process.argv[2];

/* Check if the argument is a number */
if (isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument));
}
