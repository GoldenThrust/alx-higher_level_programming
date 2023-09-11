#!/usr/bin/node
let num = process.argv[2];
if (isNaN(num)) {
     console.log("Not a number");
     return;
}
console.log('My number: ' + num);
