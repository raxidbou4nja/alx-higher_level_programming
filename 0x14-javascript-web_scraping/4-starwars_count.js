#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  try {
    const films = JSON.parse(body).results;

    for (let i = 0; i < films.length; ++i) {
      const characters = films[i].characters;

      for (let j = 0; j < characters.length; ++j) {
        const characterId = characters[j].split('/')[5];

        if (characterId === '18') {
          times += 1;
        }
      }
    }

    console.log(times);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
