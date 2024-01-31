#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
  } else {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeMovies.length);
  }
});
