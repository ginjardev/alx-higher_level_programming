#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let join = '';
      for (let j = 0; j < this.width; j++) {
        join += 'X';
      }
      console.log(join);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }
}

module.exports = Rectangle;
