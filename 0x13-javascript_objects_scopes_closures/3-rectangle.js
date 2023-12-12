#!/usr/bin/node
/* Class Rectangle that defines a rectangle  */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print a rectangle image with "X"
  print () {
    let line;
    for (let i = 0; i < this.height; i++) {
      line = 'X';
      for (let j = 0; j < this.width - 1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
