#!/usr/bin/node

/**
 * A class `Square` that defines a square and inherits from Rectangle file:
 * `4-rectangle.js`
 * The constructor takes 1 argument: size.
 * The constructor of Rectangle is called (by using super()).
 */

/* Importing the Rectangle file from file `4-rectangle.js` */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    /* Call the constructor of the Rectangle class with same size */
    super(size, size);
  }
}

module.exports = Square;
