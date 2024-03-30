#!/usr/bin/node

const { argv } = require('node:process');

function findSecondlargest (argv) {
  if (argv.length < 3) {
    return 0;
  } else if (argv.length === 3) {
    return 0;
  } else {
    const array = argv.slice(2);
    array.sort(function (a, b) {
      return parseInt(b) - parseInt(a);
    });
    return array[1];
  }
}

console.log(findSecondlargest(argv));
