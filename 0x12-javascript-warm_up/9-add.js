#!/usr/bin/node
let arg = process.argv;
function add(a, b) {
    console.log(Number(a) + Number(b));
}

add(arg[2], arg[3]);
