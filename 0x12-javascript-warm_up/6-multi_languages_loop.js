#!/usr/bin/node

if (process.argv[2]) {
  if (Number(process.argv[2]) > 0) {
    for (i = 0; i < Number(process.argv[2]); i++) {
	    console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
