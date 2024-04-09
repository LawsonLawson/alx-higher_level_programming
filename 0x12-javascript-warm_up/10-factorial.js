#!/usr/bin/node

/**
 * A script that computes and prints a factorial.
 * The first argument is integer (argument can be cast as integer) used for
 * computing the factorial.
 * Factorial of NaN is 1.
 */

/* Initialize a varible to store the casted number, thus argv[2] */
const number = parseInt(process.argv[2]);

/* Write a function to compute the factorial */
function factorial (num) {
  if (!num) {
    return (1);
  } else {
    return (num * factorial(num - 1)); /* Recursively */
  }
}
console.log(factorial(number));
