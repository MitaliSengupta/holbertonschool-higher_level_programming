#!/usr/bin/node
const newlist = require('./100-data.js').list;
console.log(newlist);
console.log(newlist.map((i, n) => i * n));
