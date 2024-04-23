#!/usr/bin/node
const request = require('request');
const process = require('process');

let id = process.argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, response, body) {
  if (err) return;
  if (response.statusCode === 200) {
    let data = JSON.parse(body);
    console.log(data.title);
  }
});
