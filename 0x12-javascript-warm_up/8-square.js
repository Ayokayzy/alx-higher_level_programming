#!/usr/bin/node

const argv = process.argv;
let square = '';

if (isNaN(argv[2]) || !argv[2]) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    for (let j = 0; j < Number(argv[2]); j++) {
      square += 'x';
    }
    if (i + 1 !== Number(argv[2])) square += '\n';
  }
}
console.log(square);
