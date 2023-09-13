#!/usr/bin/node

const dict = require('./101-data.js').dict;

const obj = {};

for (const val in dict) {
  const ocur = dict[val];

  if (obj[ocur]) {
    obj[ocur].push(val);
  } else {
    obj[ocur] = [val];
  }
}
console.log(obj);
