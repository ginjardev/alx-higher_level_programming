#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let join = '';
      for (let j = 0; j < this.width; j++) {
        join += c;
      }
      console.log(join);
    }
  }
}

module.exports = Square;
