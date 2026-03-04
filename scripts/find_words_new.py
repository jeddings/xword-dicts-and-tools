#!/usr/bin/env python3

import re
import os
import csv
import sys
import argparse

# Precompile regular expressions
WORD_REGEX = re.compile(r"\b\w+\b")

# Comparison Functions
def is_substring(find_word, found_word):
    return find_word in found_word

def is_letters_contained(find_word, found_word):
    find_word = find_word.lower()
    found_word = found_word.lower()
    find_set = set(find_word)
    found_set = set(found_word)
    return find_set.issubset(found_set)

def is_substitution_match(find_word1, find_word2, found_word):
    found_word = found_word.lower()
    found_set = set(found_word)
    replaced_set = found_set - set(find_word1.lower())
    replaced_word = ''.join(replaced_set)
    if replaced_word in all_words_set and found_word != replaced_word:
        print(f"{found_word} -> {replaced_word}")
    return replaced_word in all_words_set and found_word != replaced_word

# Main Function
def check_words(find_list, word_list, lower_bound, comparison_func):
    result = []
    for find_word1, find_word2 in find_list:
        for word, score in word_list:
            if comparison_func(find_word1, find_word2, word):
                if score >= lower_bound:
                    result.append((find_word1, find_word2, word, score))
    return result

# File and Input Functions
def read_find_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().strip().splitlines()

        find_list = []
        if len(lines) % 2 == 1:
            print("Warning: Ignoring the last word as it doesn't have a pair.")
            lines = lines[:-1]  # Ignore the last word if there are an odd number of lines

        for i in range(0, len(lines), 2):
            find_list.append((lines[i].strip(), lines[i+1].strip()))

        return find_list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: Failed to read find_words from file '{file_path}'.")
        print(f"Error details: {e}")

def read_find_words_from_string(find_words_string):
    try:
        words = find_words_string.strip().split(',')
        find_list = []

        if len(words) % 2 == 1:
            print("Warning: Ignoring the last word as it doesn't have a pair.")
            words = words[:-1]  # Ignore the last word if there are an odd number of words

        for i in range(0, len(words), 2):
            find_list.append((words[i].strip(), words[i+1].strip()))

        return find_list
    except Exception as e:
        print("Error: Failed to read find_words from the provided string.")
        print(f"Error details: {e}")

# Command Line Arguments
parser = argparse.ArgumentParser(description='Find words.')
parser.add_argument('--comp', choices=['substring', 'letters', 'substitution'], default='substitution',
                    help='Comparison function to use (default: substitution)')
parser.add_argument('filename', nargs='?', default='all-scored-high.dict',
                    help='Filename for all the words to look through (default: all-scored-high.dict)')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--find-words', metavar='WORD_PAIRS',
                   help='Word pairs to find (format: "word1, word2, word3, word4, ...")')
group.add_argument('--find-words-file', metavar='FILE_PATH',
                   help='File containing word pairs to find (format: one word pair per line)')

args = parser.parse_args()

# Load word list
try:
    with open(args.filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        word_list = [(row[0], int(row[1])) for row in reader]
except FileNotFoundError:
    print(f"Error: File '{args.filename}' not found.")
    sys.exit(1)
except Exception as e:
    print(f"Error: Failed to read word list from file '{args.filename}'.")
    print(f"Error details: {e}")
    sys.exit(1)

# Create set of all words for substitution checks
all_words_set = set(word for word, _ in word_list)

# Determine the comparison function
if args.comp == 'substring':
    comparison_func = is_substring
elif args.comp == 'letters':
    comparison_func = is_letters_contained
else:
    comparison_func = is_substitution_match

# Determine the find words
if args.find_words:
    find_list = read_find_words_from_string(args.find_words)
else:
    find_list = read_find_words_from_file(args.find_words_file)

# Check words
result = check_words(find_list, word_list, 0, comparison_func)

# Print the result
if result:
    for find_word1, find_word2, word, score in result:
        print(f"{find_word1} -> {find_word2} : {word} ({score})")
else:
    print("No matches found.")
