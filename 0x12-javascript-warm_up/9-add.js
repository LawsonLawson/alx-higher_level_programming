#!/usr/bin/node

/**
 * A script that prints the addition of 2 integers.
 * The first argument is the first integer.
 * The second argument is the second integer.
 *
 * Function prototype: function add(a, b).
 */

/* Let's save and convert both arguments to integers */
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

/* Let's define a function that returns the sum of 2 numbers, thus args */
function add (a, b) {
  const result = a + b;
  return result;
}
/* Let's compute and print the result */
console.log(add(firstArg, secondArg));
