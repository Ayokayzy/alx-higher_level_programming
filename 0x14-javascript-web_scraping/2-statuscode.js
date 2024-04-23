#!/usr/bin/node
const process = require('process');
const request = require('request');

let url = process.argv[2];

request(url, function (err, response, body) {
  if (err) return;
  console.log('code:', response && response.statusCode);
});
