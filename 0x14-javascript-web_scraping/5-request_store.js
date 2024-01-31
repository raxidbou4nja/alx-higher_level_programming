#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (_err, _res, body) {
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
