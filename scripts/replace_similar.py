#!/usr/bin/python3

import unicodedata
import sys
import fileinput
from pprint import pprint
import csv

FILENAME = ''

try:
    FILENAME = sys.argv[1]
except:
    print(f"No filename for comparison")
    quit()

def strip_accents(s):
    """String accents from a string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def read(input):
    parsed = []
    used_words = set()
    
    #    with open(input, 'r') as f:
    for line in input:
        
        # Remove leading and trailing whitespace
        line = line.strip()
        # Split out the word and score
        try:
            word, score = line.split(';')
        except:
            # continue
            word = line
            score = "-1"
    
        # Don't bother if we don't have a score
        if score is None:
            # continue
            score = "-1"
            
        # Cast score as an int
        try:
            score = int(score.strip())
        except:
            print(f"Problem with {line}")

        # Don't bother if we don't have a word
        if not word:
            continue
        
        ## Normalize the word ##
        # Strip extraneous whitespace
        word = word.strip()
        
        # Strip accents
        word = strip_accents(word)
        
        # Make uppercase
        word = word.lower()

        origWord = word
        
        # Remove any non-alphanumeric characters
        word = ''.join(c for c in word if c.isalnum())
        
        # Don't use words more than once
        if word in used_words:
            continue
        else:
            used_words.add(word)
            
        # Add this word to our collection 
        parsed.append({"word": word, "score": score, "orig_word": origWord})
    return parsed

def sort(words):
    return sorted(sorted(words, key=lambda x: x['word']), key=lambda x: x['score'])

def contains(words, check, minscore):
    con = []

    for wordPair in words:
        word = wordPair["word"]
        score = wordPair["score"]
        origWord = wordPair["orig_word"]
        
        if score < minscore:
            continue
        
        for checkPair in check:
            checkWord = checkPair["word"]
            if len(word) - 6 > len(checkWord):
                continue
            try:
                subidx = word.index(checkWord)
                if subidx >= 2 and len(checkWord) + subidx + 2 < len(word):
                    con.append({'word': word, 'check': checkWord, 'score': score, 'orig_word': origWord})
            except:
                continue
    return con
    
def replaceSimilar(words, check, minscore):
    con = []

    



    
def write(sorted_words):
    with open(FILENAME, 'w') as f:
        for w in sorted_words:
            word, score = w['word'] ,w['score']
            f.write(f'{word};{score}\n')
        print(f"Successfully sorted dictionary with {len(words)} words!")


if __name__ == '__main__':

    if sys.stdin.isatty():
        quit()
 
    words = sort(read(sys.stdin))
    # print(words)

    check = sort(read(fileinput.input()))
    # print(check)
    
    contain = contains(words, check, 60)
    # pprint(contain)

    
    quit()
    # Double-check the list is roughly as long as expected
    assert len(words) > 1000, f"Word list is too short ({len(words)} words), cancelling"

    print(words)

