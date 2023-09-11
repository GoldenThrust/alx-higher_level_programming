#!/usr/bin/node
let num = process.argv[2];
if (isNaN(num)) {
     console.log("Missing size");
     return;
}

for (let i = 0; i < num; i++) {
    let value = '';
    for (let i = 0; i < num; i++) {
        value += "x";
    }
    console.log(value);
}
