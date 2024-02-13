#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangle = '';
    let i = 0;
    while (i < this.height) {
      let j = 0;
      if (rectangle !== '') rectangle += '\n';
      while (j < this.width) {
        rectangle += 'X';
        j++;
      }
      i++;
    }
    console.log(rectangle);
  }
}
module.exports = Rectangle;
