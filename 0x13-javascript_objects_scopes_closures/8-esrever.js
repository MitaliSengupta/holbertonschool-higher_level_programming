#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  let i = list.length - 1;
  while (i >= 0) {
    reverse.push(list[i]);
    i--;
  }
  return reverse;
};
