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

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const hold = this.height;
    this.height = this.width;
    this.width = hold;
  }
}
module.exports = Rectangle;
