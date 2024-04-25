#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, body) => {
  if (err) return;

  fs.writeFile(file, body, (err) => {
    if (err) return console.log(err);
  });
  console.log(body);
});
