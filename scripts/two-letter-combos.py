#!/usr/

import csv
import nltk

# Download the CMU Pronouncing Dictionary
nltk.download('cmudict')

# Import the CMU Pronouncing Dictionary
from nltk.corpus import cmudict

# Define the letter combinations and their corresponding phonetic pronunciations
# combinations = {
#     "AB": "ay-bee",
#     "AC": "ay-see",
#     "AD": "ay-dee",
#     # Add more combinations here...
# }

# Define the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Generate the list of two-letter combinations and their phonetic pronunciations
combinations = [(a + b, f'{a.lower()}-{b.lower()}') for a in alphabet for b in alphabet]

# Print the combinations in CSV format
header = ['Combination', 'Phonetic Pronunciation']
rows = [[combination, pronunciation] for combination, pronunciation in combinations]


# Initialize the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Define the function to check if a word is an acronym or initialism
def is_acronym(word):
    return word.isupper()

# Generate the list of combinations, pronunciations, words, and confidence levels
result = []
for combination, pronunciation in combinations.items():
    word = combination.lower()  # Convert combination to lowercase to match common words
    confidence = 9  # Set the initial confidence level
    
    # Check if the resulting word is an acronym or initialism
    if is_acronym(word):
        continue  # Skip if it is an acronym or initialism
    
    # Look up words matching the given phonetic pronunciation
    matching_words = [w for w, pronunciations in pronouncing_dict.items() if [p for p in pronunciations if p == pronunciation]]
    
    # Add words to the result
    for matching_word in matching_words:
        if len(matching_word) > 2:
            result.append([combination, pronunciation, matching_word, confidence])

# Print the list
for row in result:
    print(row)
