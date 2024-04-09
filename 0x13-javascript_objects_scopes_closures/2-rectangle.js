#!/usr/bin/node

/**
 * A class `Rectangle` that defines a rectangle.
 * If w or h is equal to 0 or not a positive integer, create an empty object.
 */
class Rectangle {
  constructor (w, h) {
    /* Only assign these when w and h are greater than 0 */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
