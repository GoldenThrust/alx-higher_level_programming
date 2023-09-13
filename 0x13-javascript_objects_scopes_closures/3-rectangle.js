#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let xRect = '';
      for (let i = 0; i < this.width; i++) {
        xRect += 'X';
      }
      console.log(xRect);
    }
  }
}

module.exports = Rectangle;
