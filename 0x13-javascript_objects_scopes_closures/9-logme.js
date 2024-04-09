#!/usr/bin/node

/**
 * A function that prints the number of arguments already printed and the new
 * argument value.
 * Prototype:
 * `exports.logMe = function (item)`
 */
let totalArgs = 0;

exports.logMe = function (item) {
  console.log(totalArgs + ': ' + item);
  totalArgs++;
};
