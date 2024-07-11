#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
    console.log('Usage: ./0-starwars_characters.js <film_id>');
    process.exit(1);
}

const movieID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieID}/`;
request(url, (error, res, body) => {
    if (error) {
        console.log(error);
        return;
    }
    if (res.statusCode !== 200) {
        console.log('Failed To Get Movie');
        return;
    }
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach((character) => {
        request(character, (error, res, body) => {
            if (error) {
                console.log(error);
                return;
            }
            if (res.statusCode !== 200) {
                console.log('Failed To Get Character');
                return;
            }
            const characterName = JSON.parse(body);
            console.log(characterName.name);
        })
    })
});
