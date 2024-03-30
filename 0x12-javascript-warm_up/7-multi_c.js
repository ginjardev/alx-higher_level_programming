#!/usr/bin/node
const { argv } = require('node:process');

const value = parseInt(argv[2]);

if (!Number.isInteger(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = value; i > 0; i--) {
    console.log('C is fun');
  }
}
