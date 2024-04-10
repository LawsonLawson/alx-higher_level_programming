#!/usr/bin/node

/**
 * A script that imports an array and computes a new array.
 * A new list must be created with each value equal to the value of the initial
 * list, multipled by the index in the list
 */
/* Importing the list array from file `100-data.js` */
const list = require('./100-data').list;

/* Create a new array by multiplying each value in the list by its index */
const newList = list.map(function (number, index) {
  return number * index;
});

/* Output the orginal list array */
console.log(list);

/* Output the new array with values multiplied by their index */
console.log(newList);
