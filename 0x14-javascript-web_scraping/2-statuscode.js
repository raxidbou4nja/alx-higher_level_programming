#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./http-status.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('Code:', response.statusCode);
  }
});

