#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

const obj = {};
request(url, (err, res, data) => {
  if (err) return console.log(err);
  const resp = JSON.parse(data);
  for (let i = 0; i < resp.length; i++) {
    if (resp[i].completed) {
      obj[`${resp[i].userId}`] =
        !obj[`${resp[i].userId}`] ? 0 + 1 : Number(obj[`${resp[i].userId}`]) + 1;
    }
  }
  console.log(obj);
});
