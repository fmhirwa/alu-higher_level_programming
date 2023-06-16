#!/usr/bin/node
const req = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

req.get(url, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  console.log(`${movie.title}`);
});
