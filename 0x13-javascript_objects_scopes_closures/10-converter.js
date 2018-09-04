#!/usr/bin/node
exports.converter = function (base) {
  return function (newbase) {
    return newbase.toString(base);
  };
};
