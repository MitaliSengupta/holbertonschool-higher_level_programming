#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));
function factorial (n) {
  if (!n) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
