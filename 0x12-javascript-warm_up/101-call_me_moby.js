#!/usr/bin/node

exports.callMeMoby = function (count, func) {
  for (let i = count; i > 0; i--) {
    func();
  }
};
