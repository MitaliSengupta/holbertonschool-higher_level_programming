#!/usr/bin/node
const dictionary = require('./101-data.js').dict;
console.log(dictionary);
let newdict = {};
console.log(newdict);
for (let key in dictionary) {
  if (newdict[dictionary[key]] === undefined) {
    newdict[dictionary[key]] = [];
    console.log('you are inside if check: ' + dictionary);
    console.log('you are inside if check: ' + newdict);
  }
  newdict[dictionary[key]].push(key);
  console.log(newdict);
}
console.log(newdict);
