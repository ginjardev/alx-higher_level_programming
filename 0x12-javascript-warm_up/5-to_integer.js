#!/usr/bin/node
const { argv } = require('node:process');

let value = parseInt(argv[2])

if (Number.isInteger(value)) {
	console.log('My number: ' + value)
} else {
	console.log('Not a number')
}

