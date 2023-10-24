#!/usr/bin/node

const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('code: ' + response.statusCode);
  }
})
