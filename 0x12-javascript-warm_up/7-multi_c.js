#!/usr/bin/node
let i = 0;
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
