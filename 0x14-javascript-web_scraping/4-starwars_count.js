#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmIdx in films) {
      const characters = films[filmIdx].characters;
      for (const charIdx in characters) {
        if (characters[charIdx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. status coode: ' + response.statusCode);
  }
});
