#!/usr/bin/node
const { argv } = require('node:process');

const value = parseInt(argv[2]);

if (!Number.isInteger(value)) {
  console.log('Missing size');
} else {
  for (let i = value; i > 0; i--) {
    let join = '';
    for (let j = value; j > 0; j--) {
      join += 'X';
    }
    console.log(join);
  }
}
