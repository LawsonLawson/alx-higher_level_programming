#!/usr/bin/node
/**
 * A script that prints a message depending on the number of arguments passed.
 * If no arguments are passed to the script, it print “No argument”
 * If only one argument is passed to the script, it print “Argument found”
 * Otherwise, it print “Arguments found”
 */
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
