#!/usr/bin/node

/**
 * A a script that prints a square.
 * The first argument is the size of the square.
 * If the first argument can’t be converted to an integer, it prints:
 * “Missing size”
 */
/* Initialize a variable to store the size of the square, thus argv[2] */
const size = process.argv[2];

/* Check if the size is a numer */
if (isNaN(size)) {
  console.log('Missing size');
} else {
/* Once we get a number, we loop according to that size */
  for (let i = 0; i < size; i++) {
    console.log('XXXX');
  }
}
