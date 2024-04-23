#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) return console.log(err);
  console.log(data);
});
