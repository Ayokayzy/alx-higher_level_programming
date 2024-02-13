#!/usr/bin/node

const av = process.argv;
function add (a, b) {
  console.log(Number(a) + Number(b));
}

add(av[2], av[3]);
