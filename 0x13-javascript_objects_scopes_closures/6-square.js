#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    let i = 0;
    while (i < this.height) {
      let j = 0;
      if (square !== '') square += '\n';
      while (j < this.width) {
        square += c || 'X';
        j++;
      }
      i++;
    }
    console.log(square);
  }
}

module.exports = Square;
