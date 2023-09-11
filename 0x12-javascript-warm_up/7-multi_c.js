#!/usr/bin/node
let num = process.argv[2];
if (isNaN(num)) {
     console.log("Missing number of occurrences");
     return;
}

for (let i = 0; i < num; i++) {
    console.log('C is fun');
}
