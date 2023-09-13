#!/usr/bin/node
const eSquare = require('./5-square.js');

class Square extends eSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let cSqu = '';
      for (let i = 0; i < this.width; i++) {
        cSqu += c;
      }
      console.log(cSqu);
    }
  }
}

module.exports = Square;
