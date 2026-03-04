#!/usr/local/bin/node

var _ = require("underscore.string");
var glob = require("glob");
var fs = require("fs");
var async = require("async");
var sync = require("synchronize");

var await = sync.await;
var defer = sync.defer;

var DIR_PATH = "/Users/jeddings/Documents/Crosswords/Dictionaries";
var MIN_SCORE = 40;

// get the list of words
var fileGlob = DIR_PATH + "/" + "s*.dict";

var lines = [];
var words = new Object();
var successWords = new Object();

sync(fs, 'readFile');

sync.fiber(function() {
    var data = fs.readFile(__filename, "utf8");
    console.log(data);
});



function processDicts() {
    var self = this;
    self.processWords();
}

processDicts.prototype.processWords = function() {
    var self = this;
    self.readDictFiles();

}

processDicts.prototype.readDictFiles = function() {
    var self = this;
    
    glob(fileGlob, function(err, files) {
        if (err) return console.error(err);

        async.eachSeries(files, self.processFile, function() {
            console.log("I am done");
        }

                         for (var file in files) {


                         }}}}}

processDicts.prototype.processFile = function(file, callback) {
    var self = this;

    async.waterfall([
        function(callback) {
            fs.readFileSync(file, "utf8", function(err, data) {
                lines[] = _(data.toLowerCase()).trim().clean().cleanDiacritics().lines();
            })
        },
        function(callback) {
            
        }
        
    ]);

}
            })
        }
    })
    
    self.processLines();
}

processDicts.prototype.processLines = function() {
    var self = this;
    
    for (var line in lines) {
        word = _(line.toString()).strLeft("\;").value().replace(/[^a-z]/g, "");
        score = parseInt(_(line).strRight("\;").value());
        if (score > MIN_SCORE) {
            //console.log(word);
            words[word] = score;
            console.log(word + "=" + words[word]);
        }                       
    }
}



glob(fileGlob, function(err, files) {
    if (err) return console.error(err);
    
    var line = "";
    var word = "";
    var score = 0;
    var numIter = files.length;
        
    for (i = 0; i < numIter; i++) {
        fs.readFile(files[i], "utf8", function (err, data) {
            //console.log(data);
            if (err) { console.log(err); }
            
            lines = _(data.toLowerCase()).trim().lines(); // S.slugify(data) + "";
            for (j = 0; j < lines.length; j++) {
                line = _(lines[j].toString()).clean().trim().cleanDiacritics().value();
                word = _(lines[j].toString()).strLeft("\;").value().replace(/[^a-z]/g, "");
                score = parseInt(_(lines[j]).strRight("\;").value());
                if (score > MIN_SCORE) {
                    //console.log(word);
                    words[word] = score;
                    console.log(word + "=" + words[word]);
                }               
            }
        });
    }

    console.log("words length = " + words.length);
        
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

function readAndCreateWordsHash() {
    
}

function performAction(word) {
    

}
