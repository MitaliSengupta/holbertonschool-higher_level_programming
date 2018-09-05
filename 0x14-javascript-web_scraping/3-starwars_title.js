#!/usr/bin/node
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2] + '/', function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
