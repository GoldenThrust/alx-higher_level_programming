#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);

    for (const i in tasks) {

      if (tasks[i].completed) {

        if (completed[tasks[i].userId]) {
          completed[tasks[i].userId]++;
        } else {
          completed[tasks[i].userId] = 1;
        }

      }
    
    }
    console.log(completed);
  } else {
    console.log('code: ' + response.statusCode);
  }
})
