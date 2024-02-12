#!/usr/bin/node

if (String(Number(process.argv[2])) !== 'NaN') {
  console.log(`My Number: ${Number(process.argv[2])}`);
} else {
  console.log('Not a number');
}
