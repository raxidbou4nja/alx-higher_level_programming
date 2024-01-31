#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  try {
    const characterUrls = JSON.parse(body).characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error('Error:', charError.message);
        } else {
          const charName = JSON.parse(charBody).name;
          console.log(charName);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
