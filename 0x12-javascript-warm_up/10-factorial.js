#!/usr/bin/node

const { argv } = require('node:process');

const value = parseInt(argv[2]);

function factorial (value) {
  if (Number.isNaN(value)) {
    return 1;
  } else if (value === 0) {
    return 1;
  }

  return value * factorial(value - 1);
}
console.log(factorial(value));
