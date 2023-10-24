#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body).results;
    let i = 0;

    for (const j in responseJSON) {
      const characters = responseJSON[j].characters;
      for (const k in characters) {
        if (characters[k].includes('18')) {
          i++;
        }
      }
    }

    console.log(i);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
