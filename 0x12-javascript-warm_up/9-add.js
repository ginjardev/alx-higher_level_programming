#!/usr/bin/node

const { argv } = require('node:process');

const value1 = parseInt(argv[2]);
const value2 = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(value1, value2);
