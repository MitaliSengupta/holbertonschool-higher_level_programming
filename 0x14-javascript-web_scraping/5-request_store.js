#!/usr/bin/node
let fs = require('fs');
let request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  else {
    fs.writeFile(process.argv[3], body, 'utf8');
  }
});
