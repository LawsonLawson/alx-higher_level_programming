#!/usr/bin/node

/**
 * A function that returns the addition of 2 integers.
 *
 * Note: This lad here is exported as a known function, thus:
 * exports.<name of funtion> = blah blah
 */
exports.add = function add (x, y) {
  const result = parseInt(x) + parseInt(y);
  return result;
};
