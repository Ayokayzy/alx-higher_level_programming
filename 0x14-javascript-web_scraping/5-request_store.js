#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, body) => {
  if (err) return;

  fs.writeFile(file, body, { encoding: 'utf-8' }, (err) => {
    if (err) return console.log(err);
  })
})
