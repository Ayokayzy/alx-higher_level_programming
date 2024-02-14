#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list.filter(element => element === searchElement);
  return arr.length;
};
