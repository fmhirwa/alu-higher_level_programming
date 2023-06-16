#!/usr/bin/node

const request = require('request');
let xFilms = 0;

request(process.argv[2], function (err, res, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          xFilms++;
        }
      }
    }
  }
  console.log(xFilms);
});
