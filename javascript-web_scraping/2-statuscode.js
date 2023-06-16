#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], function (error, result) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ' + result.statusCode);
});
