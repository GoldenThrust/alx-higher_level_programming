#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);

    for (const i of responseJSON.characters) {
      request.get(i, (cError, cResponse, cBody) => {
        const resp = JSON.parse(cBody);
        console.log(resp.name);
      });
    }
  } else {
    console.log('code: ' + response.statusCode);
  }
});
