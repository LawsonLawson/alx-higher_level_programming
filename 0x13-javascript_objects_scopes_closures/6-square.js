#!/usr/bin/node

/**
 * A class `Square` that defines a square and inherits from `Square` of file:
 * `5-square.js`
 * Creates an instance method that prints the rectangle using the character c.
 * If c is undefined, use the character X.
 */

/* Importing the Square class */
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      /* Default to 'X' if c is undefined */
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square = square + c;
      }
      console.log(square);
    }
  }
}

module.exports = Square;
