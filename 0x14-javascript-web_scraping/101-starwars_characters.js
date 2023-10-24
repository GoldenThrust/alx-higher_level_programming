#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    await printAllCharacters(characters);
  }
});

async function printAllCharacters (characters) {
  for (let i = 0; i < characters.length; i++) {
    try {
      const characterData = await makeRequest(characters[i]);
      console.log(characterData);
    } catch (error) {
      console.error(error);
    }
  }
}

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data.name);
      } else {
        reject(error);
      }
    });
  });
}
