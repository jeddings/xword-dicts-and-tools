#!/usr/local/bin/node

var glob = require('glob')({gitignore: true});

// get the list of words
glob('/Users/jeddings/Crosswords/Dictionaries/*.dict', function(err, files) {
    //if (err) return console.error(err);
    //console.log("hello");
    //console.log(files);
});

// filter for score

// lowercase

// put list into memory using hash table { word => 0 }

// go through list of words

// find pattern

// do operation (replace, move, etc.)

// look for new word in hash table

// put into hash table { word => 1 }

// go through hash table and output any words with 1

