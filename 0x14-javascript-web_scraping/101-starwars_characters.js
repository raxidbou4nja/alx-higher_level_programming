#!/usr/bin/node

const request = require('request');

function getDataFrom(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function printMovieCharacters(movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  try {
    const movieData = await getDataFrom(movieUri);
    const { characters } = JSON.parse(movieData);

    const characterPromises = characters.map(characterUrl => getDataFrom(characterUrl));
    const characterResponses = await Promise.all(characterPromises);

    const characterNames = characterResponses.map(response => JSON.parse(response).name);
    characterNames.forEach(name => console.log(name));
  } catch (err) {
    console.log(err);
  }
}

printMovieCharacters(process.argv[2]);
