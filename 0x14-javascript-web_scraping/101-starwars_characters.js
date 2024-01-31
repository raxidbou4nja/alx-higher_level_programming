#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
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

function errHandler (err) {
  console.log(err);
}

async function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  try {
    const movieData = await getDataFrom(movieUri);
    const characters = JSON.parse(movieData).characters;

    const characterPromises = characters.map(characterUrl => getDataFrom(characterUrl));
    const characterResponses = await Promise.all(characterPromises);

    characterResponses.forEach(response => {
      console.log(JSON.parse(response).name);
    });
  } catch (err) {
    errHandler(err);
  }
}

printMovieCharacters(process.argv[2]);
