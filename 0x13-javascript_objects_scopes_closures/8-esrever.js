#!/usr/bin/node

/**
 * A function that returns the reversed version of a list.
 * Prototype:
 * `exports.esrever = function (list)`
 */
exports.esrever = function (list) {
  let i = 0;
  let length = list.length - 1;

  while ((length - i) > 0) {
    const swap = list[length]; /* Swap */
    list[length] = list[i];
    list[i] = swap;
    i++;
    length--;
  }
  return list;
};
