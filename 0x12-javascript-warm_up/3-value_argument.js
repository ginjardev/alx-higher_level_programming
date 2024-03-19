#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('No argument');
} else {
  argv.forEach((x) => console.log(x));
}
