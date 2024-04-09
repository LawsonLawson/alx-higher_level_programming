#!/usr/bin/node

/**
 * A script that prints x times “C is fun”.
 * Where x is the first argument of the script.
 * If the first argument can’t be converted to an integer, it prints:
 * “Missing number of occurrences”
 */
/* Number of times to print the statement, thus x */
const argument = process.argv[2];

/* Check if the argument is undefined or is a number */
if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
/* We loop 'argument' number of times ... */
  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
}
