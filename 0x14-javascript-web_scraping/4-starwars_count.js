#!/usr/bin/node
const request = require('request');
const process = require('process');

let url = process.argv[2];

request(url, function (err, response, body) {
  if (err) return;
  if (response.statusCode === 200) {
    let data = JSON.parse(body);
    let count = 0;
    for (let item of data.results) {
      for (let actor of item.characters) {
        let actorSplit = actor.split('/');
        let actorId = actorSplit[actorSplit.length - 2];
        if (actorId === '18') {
          count++;
        }
      }
    };
    console.log(count);
  }
});
