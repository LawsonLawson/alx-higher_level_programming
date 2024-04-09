#!/usr/bin/node

/**
 * A class `Rectangle` that defines a rectangle.
 * If w or h is equal to 0 or not a positive integer, create an empty object.
 * Creates an instance method that prints the rectangle using the character X.
 */

class Rectangle {
  constructor (w, h) {
    /* Checks for wether h or w is greater than 0 */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle = rectangle + 'X';
      }
      console.log(rectangle);
    }
  }
}

module.exports = Rectangle;
