#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      num++;
    }
  }
  return num;
};
