#!/usr/bin/node

/**
 * A script that searches the second biggest integer in the list of arguments.
 * If no argument is passed, prints 0.
 * If the number of arguments is 1, prints 0.
 */

/* Convert the arguments to integers */
const args = process.argv.slice(2).map(Number);

/* If no argument or onluy one argument is passed, print 0 to the console */
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  /* Sort the arguments in descending order, thus high to low */
  args.sort((a, b) => b - a);

  /* Find the second largest integer */
  const secondLargest = args[1];

  /* Print the second largest integer to the console */
  console.log(secondLargest); // Print the second largest integer
}
