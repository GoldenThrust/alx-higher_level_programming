#!/usr/bin/node
const arg = process.argv.slice(2).map(Number);

if (arg.length > 1) {
  console.log(arg.sort().reverse()[1]);
} else {
  console.log(0);
}
