#!/usr/bin/node

/**
 * A class `Rectangle` that defines a rectangle.
 * The constructor takes 2 arguments: w and h.
 * Initialized the instance attribute width with the value of w.
 * Initialized the instance attribute height with the value of h.
 * If w or h is equal to 0 or not a positive integer, it create an empty object
 * Creates an instance method called print() that prints the rectangle using
 * the character X.
 * Creates an instance method called rotate() that exchanges the width and the
 * height of the rectangle.
 * Creates an instance method called double() that multiples the width and the
 * height of the rectangle by 2.
 */

/* Class Creation */
class Rectangle {
  constructor (w, h) {
    /* Check for wether h and w are greater than 0 before initialization */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* A method that prints a rectangle using the X character */
  print () {
    /* Printing the height of the rectangle */
    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle = rectangle + 'X';
      }
      /* Print the rectangle */
      console.log(rectangle);
    }
  }

  /* A method that exchanges the width and the height values */
  rotate () {
    const swap = this.height; /* Put the value of h in swap */
    this.height = this.width; /* Put the value of h in w */
    this.width = swap; /* Put the value of swap, thus h in width */
  }

  /* A method that multiplies the width and the height */
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
