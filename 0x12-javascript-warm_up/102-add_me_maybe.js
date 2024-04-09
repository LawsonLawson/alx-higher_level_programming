#!/usr/bin/node

/**
 * This function increments and makes a function call.
 */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
