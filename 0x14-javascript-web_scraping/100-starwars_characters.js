#!/usr/bin/node
let request = require('request');
let api = 'https://swapi.co/api/films/';
request.get(api + process.argv[2], function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    let everything = JSON.parse(body);
    for (let ch of everything.characters) {
      request.get(ch, function (err, response, body) {
        let everything = JSON.parse(body);
        if (err) throw err;
        else if (response.statusCode === 200) { console.log(everything.name); }
      });
    }
  }
});
