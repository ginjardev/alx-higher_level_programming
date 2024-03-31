#!/usr/bin/node

exports.addMeMaybe = function (count, func) {
  count++;
  func(count);
};
