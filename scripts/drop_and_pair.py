#!/usr/local/bin/python3

import re

def find_word_pairs(filename, search_word):
    word_list = []
    word_pairs = []

    # Read the word list file and store the words in a list
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().upper()
            word = re.sub(r'[^A-Z;0-9]', '', word)
            pair = word.split(";")
            try:
                if int(pair[1]) >= min_score:
                    word_list.append(pair[0])
#                     print(pair[0], " → ", pair[1])
#                 print("Converted value:", number)
            except ValueError:
                print("Error: Cannot convert string to integer")
                

    # Convert search word to all caps and strip out non-alphabetic characters
    search_word = re.sub(r'[^A-Z]', '', search_word.upper())

    # Find words in the word list that contain the search word at the front or the end
#     matching_words = [word for word in word_list if word.startswith(search_word) or word.endswith(search_word)]
    matching_words = []
    for word in word_list:
#         if word.startswith(search_word) or word.endswith(search_word):
        if word.endswith(search_word):
            matching_words.append(word.replace(search_word, ''))

    # Find pairs of words that form valid words when combined
    for word1 in matching_words:
        for word2 in matching_words:
            if word1 != word2 and word1 != '' and word2 != '' and len(word1 + word2) > 8:
#                 print(word1, " ", word2)
                combined_word = (word1 + word2).replace(search_word, '')  # Strip off the search word
#                 print("-- ", combined_word)
                if combined_word in word_list:
                    word_pairs.append((word1, word2))
#                     print(word_pairs)

    return word_pairs



# Example usage:
filename = '../XwiWordList.dict'  # Replace with the actual filename
search_word = 'RUN'   # Replace with the word to search for
min_score = 80

pairs = find_word_pairs(filename, search_word)
print("Word pairs for", search_word, ":")
for pair in pairs:
    print(pair[0], "+", pair[1], "=", pair[0] + pair[1])