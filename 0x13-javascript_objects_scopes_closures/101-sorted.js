#!/usr/bin/node
const dictionary = require('./101-data.js').dict;
let newdict = {};
for (let key in dictionary) {
  if (newdict[dictionary[key]] === undefined) {
    newdict[dictionary[key]] = [];
  }
  newdict[dictionary[key]].push(key);
}
console.log(newdict);
