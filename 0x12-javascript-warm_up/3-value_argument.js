#!/usr/bin/node
/**
 * A script that prints the first argument passed to it.
 * If no arguments are passed to the script, it print “No argument”
 */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
