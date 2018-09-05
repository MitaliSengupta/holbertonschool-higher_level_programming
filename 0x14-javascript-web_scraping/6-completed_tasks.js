#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let done = {};
    for (let task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in done) { done[task.userId] += 1; } else { done[task.userId] = 1; }
      }
    }
    console.log(done);
  }
});
