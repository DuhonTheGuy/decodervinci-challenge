const R = require('ramda');

const chars = `ghaoodlvuefckun`;
const mask = `^..^^^^.^..^^..`;

const partA = R.zip(chars, mask).map(([c,m]) => m == '^' ? c : '').join("")
const partB = R.zip(chars, mask).map(([c,m]) => m == '.' ? c : '').join("")

console.log(partA, partB)