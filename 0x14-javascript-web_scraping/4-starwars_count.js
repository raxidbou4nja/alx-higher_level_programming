#!/usr/bin/node

const request = require('request');

const starWarsUri = 'https://swapi-api.alx-tools.com/api/films/';

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    let times = 0;

    films.forEach((film) => {
      const characters = film.characters;

      characters.forEach((character) => {
        const characterId = character.split('/')[5];

        if (characterId === '18') {
          times += 1;
        }
      });
    });

    console.log(times);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
