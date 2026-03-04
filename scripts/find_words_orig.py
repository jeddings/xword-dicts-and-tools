#!/usr/bin/env python3

import re
import os
import csv
import sys
import argparse
import string
import datetime

# Comparison Functions

def is_substring(find_word, found_word):
    """
    Check if find_word is a substring of found_word.

    Args:
        find_word (str): Word to find.
        found_word (str): Word to search within.

    Returns:
        bool: True if find_word is a substring of found_word, False otherwise.
    """
    return found_word.find(find_word) != -1 and found_word.index(find_word) != 0 and found_word.index(find_word) != (len(found_word) - len(find_word)), ''

def is_letters_contained(find_word, found_word):
    """
    Check if all letters of find_word are contained in found_word (order does not matter).

    Args:
        find_word (str): Word to find.
        found_word (str): Word to search within.

    Returns:
        bool: True if all letters of find_word are contained in found_word, False otherwise.
    """
    find_word = find_word.lower()
    found_word = found_word.lower()
    i, j = 0, 0
    while i < len(find_word) and j < len(found_word):
        if find_word[i] == found_word[j]:
            i += 1
        j += 1
    return i == len(find_word), ''

def add_prefix(find_word, found_word):
    """
    Check if found_word can be obtained by adding the substring find_word to the beginning,
    and the resulting word is not the same as found_word and is found in all_words_set.

    Args:
        find_word (str): Word to add.
        found_word (str): Word to search within.

    Returns:
        bool: True if found_word can be obtained by adding find_word to the beginning and the resulting word is not the same as found_word and is found in all_words_set, False otherwise.
    """
    found_word = found_word.lower()
    modified_word = find_word.lower() + found_word
    return modified_word != found_word and modified_word in all_words_set, modified_word

def is_substitution_match(find_word1, find_word2, found_word):
    """
    Check if found_word can be obtained by substituting find_word1 with find_word2.

    Args:
        find_word1 (str): Word to find.
        find_word2 (str): Word to substitute.
        found_word (str): Word to search within.

    Returns:
        bool: True if found_word can be obtained by substituting find_word1 with find_word2 and the resulting word is in all_words_set, False otherwise.
    """
    found_word = found_word.lower()
    found_word_replaced = found_word.replace(find_word1.lower(), find_word2.lower())
    return found_word_replaced in all_words_set and found_word != found_word_replaced, found_word_replaced

def is_drop_string(find_word, found_word):
    """
    Check if found_word can be obtained by removing the substring find_word,
    and the resulting word is not the same as found_word and is found in all_words_set.

    Args:
        find_word (str): Word to remove.
        found_word (str): Word to search within.

    Returns:
        bool: True if found_word can be obtained by removing find_word and the resulting word is not the same as found_word and is found in all_words_set, False otherwise.
    """
    found_word = found_word.lower()
    found_word_removed = found_word.replace(find_word.lower(), "")
    return found_word_removed != found_word and found_word_removed in all_words_set, found_word_removed

# Main Function

def is_drop_string_inside(find_word, found_word):
    """
    Check if found_word can be obtained by removing the substring find_word,
    and the resulting word is not the same as found_word and is found in all_words_set.

    Args:
        find_word (str): Word to remove.
        found_word (str): Word to search within.

    Returns:
        bool: True if found_word can be obtained by removing find_word and the resulting word is not the same as found_word and is found in all_words_set, False otherwise.
    """
    found_word = found_word.lower()
    find_word = find_word.lower()

    if found_word.startswith(find_word) or found_word.endswith(find_word):
#         print(f"{find_word}, {found_word}")
        return False, found_word

    found_word_removed = found_word.replace(find_word, "")
    return found_word_removed != found_word and found_word_removed in all_words_set, found_word_removed
    



def check_words(find_list, word_list, lower_bound, similarity_threshold, comparison_func):
    """
    Check for word matches based on the provided find_list and comparison function.

    Args:
        find_list (list): List of word pairs to find.
        word_list (list): List of all words to search through.
        lower_bound (int): Lower bound score for a word to be considered a match.
        similarity_threshold (float): Similarity threshold for semantic similarity comparison (not used in the current code).
        comparison_func (function): Comparison function to use for matching.

    Returns:
        list: List of matching word pairs and their corresponding scores.
    """

    result = []
    for find_words in find_list:
        if len(find_words) == 2:
            find_word1, find_word2 = find_words
        else:
            find_word1 = find_words
#             continue
        comparison_result = []
        
        for i in range(len(word_list)):
#             for j in range(i + 1, len(word_list)):
            word1, score1 = word_list[i]
#                 word2, score2 = word_list[j]
    
            if comparison_func == is_substitution_match:
                comparison_result = comparison_func(find_word1, find_word2, word1)
                if comparison_result[0]:
                    if score1 >= lower_bound:
                        result.append((find_word1, find_word2, word1, score1, comparison_result[1]))
#                     if comparison_func(find_word1, find_word2, word2):
#                         if score2 >= lower_bound:
#                             result.append((find_word1, find_word2, word2, score2))
            else:
                comparison_result = comparison_func(find_word1, word1)
                if comparison_result[0]:
                    if score1 >= lower_bound:
#                         print(f"{find_word1}, {word1}, {comparison_result[1]}")
                        result.append((find_word1, word1, score1, comparison_result[1]))
#                     if comparison_func(find_word1, word2):
#                         if score2 >= lower_bound:
#                             result.append((find_word1, word2, score2))
            
            # Check the reverse combination as well
            if comparison_func == is_substitution_match:
                comparison_result = comparison_func(find_word2, find_word1, word1)
                if comparison_result[0]:
                    if score1 >= lower_bound:
                        result.append((find_word2, find_word1, word1, score1, comparison_result[1]))
#                     if comparison_func(find_word2, find_word1, word2):
#                         if score2 >= lower_bound:
#                             result.append((find_word2, find_word1, word2, score2))
            else:
                comparison_result = comparison_func(find_word1, word1)
                if comparison_result[0]:
                    if score1 >= lower_bound:
                        result.append((find_word1, word1, score1, comparison_result[1]))
#                     if comparison_func(find_word2, word2):
#                         if score2 >= lower_bound:
#                             result.append((find_word2, word2, score2))
                            
    # Remove duplicates from the result list
    result = list(set(result))
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
parser.add_argument('--comp', choices=['substring', 'letters', 'substitution', 'drop_string', 'drop_string_inside', 'add_prefix'], default='substitution',
                    help='Comparison function to use (default: substitution)')
parser.add_argument('filename', nargs='?', default='all-scored-medium.dict',
                    help='Filename for all the words to look through (default: all-scored-medium.dict)')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--find-words', metavar='WORD_PAIRS',
                   help='Comma-delimited string of word pairs to find (e.g., "word1,word2;word3,word4")')
group.add_argument('--find-words-file', metavar='FILE_PATH',
                   help='Path to the file containing word pairs to find')
parser.add_argument('--limit', metavar='LIMIT', default='0', type=int,
                    help='Number of results to display. To show all results, use 0. (default: 0)')
parser.add_argument('--min-score', metavar='MIN_SCORE', default='60', type=int,
                    help='Minimum score to return. (default: 60)')
                   

args = parser.parse_args()

# Determine the comparison function based on the provided argument
comparison_func = None
comparison_func_name = None
if args.comp == 'substring':
    comparison_func = is_substring
    comparison_func_name = 'Substring Match (Check if find_word is a substring of found_word)'
elif args.comp == 'letters':
    comparison_func = is_letters_contained
    comparison_func_name = 'Letters Contained (Check if all letters of find_word are contained in found_word)'
elif args.comp == 'substitution':
    comparison_func = is_substitution_match
    comparison_func_name = 'Substitution Match (Check if found_word can be obtained by substituting find_word1 with find_word2)'
elif args.comp == 'drop_string':
    comparison_func = is_drop_string
    comparison_func_name = 'Drop String (Check if find_word substring is removed from found_word, and the resulting word is not the same as found_word, and is found in the all_words_set)'
elif args.comp == 'drop_string_inside':
    comparison_func = is_drop_string_inside
    comparison_func_name = 'Drop String Inside (Check if find_word substring is removed from found_word, find_word is not at the beginning or end of found_word, and the resulting word is not the same as found_word, and is found in the all_words_set)'
elif args.comp == 'add_prefix':
    comparison_func = add_prefix
    comparison_func_name = 'Add Prefix (Check if find_word is prepended to found_word, the resulting word is found in all_words_set)'

# Set the filename for all the words to look through
filename = args.filename

# Prompt the user to confirm the values before proceeding
print("Confirmation:")
print(f"Comparison function: {comparison_func_name}")
print(f"Filename: {filename}")
if args.find_words:
    print(f"Word pairs to find: {args.find_words}")
elif args.find_words_file:
    print(f"Word pairs file: {args.find_words_file}")
print(f"Results limit: {args.limit}")
print(f"Minimum score: {args.min_score}")
confirmation = input("Proceed with the above values? (y/n): ")

if confirmation.lower() != 'y':
    print("Aborted.")
    sys.exit(0)

# Read all words from the file
word_list_file = filename
if os.path.isfile(word_list_file):
    with open(word_list_file, 'r') as file:
        word_list = [line.strip().split(';') for line in file]
else:
    print(f"Error: File '{word_list_file}' not found.")
    sys.exit(1)

# Convert scores to integers
word_list = [(word, int(score)) for word, score in word_list]

# Create a set of all words for efficient lookup
all_words_set = {re.sub(r'[^a-zA-Z]', '', word.lower()) for word, _ in word_list}

# Print the number of words in all_words
print(f"Number of words in word_list: {len(word_list)}")
print(f"Number of words in all_words_set: {len(all_words_set)}")

# Read word pairs to find
if args.find_words:
    find_list = read_find_words_from_string(args.find_words)
else:
    find_words_file_path = args.find_words_file
    find_list = read_find_words_from_file(find_words_file_path)

lower_bound = args.min_score

# Call the check_words function with the provided lists and chosen comparison function
found_words = check_words(find_list, word_list, lower_bound, similarity_threshold=0.5, comparison_func=comparison_func)

# Print the number of words in found_words
print(f"Number of found words: {len(found_words)}")

lambda_val = 2
if comparison_func == is_substitution_match:
    lambda_val = 3
    
# Sort the found_words list in descending order of score, then descending order of word length
found_words.sort(key=lambda x: (x[lambda_val], -len(x[0])), reverse=True)

# Limit the number of words to be printed
if args.limit != 0:
    found_words = found_words[:args.limit]
    
print(f"len = {len(found_words)}")

# Print the found_words list
if comparison_func == is_substitution_match:
    for find_word1, find_word2, word, score, modified_word in found_words:
        print(f"{find_word1}/{find_word2}, {word}, {modified_word}, {score}")
else:
    for find_word1, word, score, modified_word in found_words:
#         print(f"Find Word: {find_word1}, Found Word: {word}, Modified Word: {modified_word}, Score: {score}")
        print(f"{find_word1}, {word}, {modified_word}, {score}")
    
# Print the results in CSV format
print("Printing results in CSV format:")
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as a string
timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")

# Append the timestamp to the filename
csv_filename = f"found_words_{timestamp}.csv"

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Find Word 1", "Find Word 2", "Found Word", "Modified Word", "Score"])
    if comparison_func == is_substitution_match:
        for find_word1, find_word2, word, score, modified_word in found_words:
            writer.writerow([find_word1, find_word2, word, modified_word, score])
    else:
        for find_word1, word, score, modified_word in found_words:
            writer.writerow([find_word1, '', word, modified_word, score])        

print("Process complete.")


# #!/usr/bin/env python3
# 
# import re
# import os
# import csv
# import sys
# import argparse
# import string
# 
# # Comparison Functions
# 
# def is_substring(find_word, found_word):
#     """
#     Check if find_word is a substring of found_word.
# 
#     Args:
#         find_word (str): Word to find.
#         found_word (str): Word to search within.
# 
#     Returns:
#         bool: True if find_word is a substring of found_word, False otherwise.
#     """
#     return found_word.find(find_word) != -1 and found_word.index(find_word) != 0 and found_word.index(find_word) != (len(found_word) - len(find_word))
# 
# def is_letters_contained(find_word, found_word):
#     """
#     Check if all letters of find_word are contained in found_word (order does not matter).
# 
#     Args:
#         find_word (str): Word to find.
#         found_word (str): Word to search within.
# 
#     Returns:
#         bool: True if all letters of find_word are contained in found_word, False otherwise.
#     """
#     find_word = find_word.lower()
#     found_word = found_word.lower()
#     i, j = 0, 0
#     while i < len(find_word) and j < len(found_word):
#         if find_word[i] == found_word[j]:
#             i += 1
#         j += 1
#     return i == len(find_word)
# 
# def is_substitution_match(find_word1, find_word2, found_word):
#     """
#     Check if found_word can be obtained by substituting find_word1 with find_word2.
# 
#     Args:
#         find_word1 (str): Word to find.
#         find_word2 (str): Word to substitute.
#         found_word (str): Word to search within.
# 
#     Returns:
#         bool: True if found_word can be obtained by substituting find_word1 with find_word2 and the resulting word is in all_words_set, False otherwise.
#     """
#     found_word = found_word.lower()
#     found_word_replaced = found_word.replace(find_word1.lower(), find_word2.lower())
# #     if found_word_replaced in all_words_set and found_word != found_word_replaced:
# #         print(f"{found_word} → {found_word_replaced}")
#         
#     return found_word_replaced in all_words_set and found_word != found_word_replaced
# 
# # Main Function
# 
# def check_words(find_list, word_list, lower_bound, similarity_threshold, comparison_func):
#     """
#     Check for word matches based on the provided find_list and comparison function.
# 
#     Args:
#         find_list (list): List of word pairs to find.
#         word_list (list): List of all words to search through.
#         lower_bound (int): Lower bound score for a word to be considered a match.
#         similarity_threshold (float): Similarity threshold for semantic similarity comparison (not used in the current code).
#         comparison_func (function): Comparison function to use for matching.
# 
#     Returns:
#         list: List of matching word pairs and their corresponding scores.
#     """
# 
#     result = []
#     for find_word1, find_word2 in find_list:
#         for i in range(len(word_list)):
#             for j in range(i + 1, len(word_list)):
#                 word1, score1 = word_list[i]
#                 word2, score2 = word_list[j]
#                 if comparison_func(find_word1, find_word2, word1):
#                     if score1 >= lower_bound:
#                         result.append((find_word1, find_word2, word1, score1))
#                 if comparison_func(find_word1, find_word2, word2):
#                     if score2 >= lower_bound:
#                         result.append((find_word1, find_word2, word2, score2))
# 
#                 # Check the reverse combination as well
#                 if comparison_func(find_word2, find_word1, word1):
#                     if score1 >= lower_bound:
#                         result.append((find_word2, find_word1, word1, score1))
#                 if comparison_func(find_word2, find_word1, word2):
#                     if score2 >= lower_bound:
#                         result.append((find_word2, find_word1, word2, score2))
# 
#     # Remove duplicates from the result list
#     result = list(set(result))
#     return result
# 
# # File and Input Functions
# 
# def read_find_words_from_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             lines = file.read().strip().splitlines()
# 
#         find_list = []
#         if len(lines) % 2 == 1:
#             print("Warning: Ignoring the last word as it doesn't have a pair.")
#             lines = lines[:-1]  # Ignore the last word if there are an odd number of lines
# 
#         for i in range(0, len(lines), 2):
#             find_list.append((lines[i].strip(), lines[i+1].strip()))
# 
#         return find_list
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"Error: Failed to read find_words from file '{file_path}'.")
#         print(f"Error details: {e}")
# 
# def read_find_words_from_string(find_words_string):
#     try:
#         words = find_words_string.strip().split(',')
#         find_list = []
# 
#         if len(words) % 2 == 1:
#             print("Warning: Ignoring the last word as it doesn't have a pair.")
#             words = words[:-1]  # Ignore the last word if there are an odd number of words
# 
#         for i in range(0, len(words), 2):
#             find_list.append((words[i].strip(), words[i+1].strip()))
# 
#         return find_list
#     except Exception as e:
#         print("Error: Failed to read find_words from the provided string.")
#         print(f"Error details: {e}")
# 
# 
# # Command Line Arguments
# 
# parser = argparse.ArgumentParser(description='Find words.')
# parser.add_argument('--comp', choices=['substring', 'letters', 'substitution'], default='substitution',
#                     help='Comparison function to use (default: substitution)')
# parser.add_argument('filename', nargs='?', default='all-scored-high.dict',
#                     help='Filename for all the words to look through (default: all-scored-high.dict)')
# group = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('--find-words', metavar='WORD_PAIRS',
#                    help='Comma-delimited string of word pairs to find (e.g., "word1,word2;word3,word4")')
# group.add_argument('--find-words-file', metavar='FILE_PATH',
#                    help='Path to the file containing word pairs to find')
# 
# args = parser.parse_args()
# 
# # Determine the comparison function based on the provided argument
# comparison_func == None
# comparison_func_name = None
# if args.comp == 'substring':
#     comparison_func == is_substring
#     comparison_func_name = 'Substring Match (Check if find_word is a substring of found_word)'
# elif args.comp == 'letters':
#     comparison_func == is_letters_contained
#     comparison_func_name = 'Letters Contained (Check if all letters of find_word are contained in found_word)'
# elif args.comp == 'substitution':
#     comparison_func == is_substitution_match
#     comparison_func_name = 'Substitution Match (Check if found_word can be obtained by substituting find_word1 with find_word2)'
# 
# # Set the filename for all the words to look through
# filename = args.filename
# 
# # Prompt the user to confirm the values before proceeding
# print("Confirmation:")
# print(f"Comparison function: {comparison_func_name}")
# print(f"Filename: {filename}")
# if args.find_words:
#     print(f"Word pairs to find: {args.find_words}")
# elif args.find_words_file:
#     print(f"Word pairs file: {args.find_words_file}")
# confirmation = input("Proceed with the above values? (y/n): ")
# 
# if confirmation.lower() != 'y':
#     print("Aborted.")
#     sys.exit(0)
# 
# # Read all words from the file
# word_list_file = filename
# if os.path.isfile(word_list_file):
#     with open(word_list_file, 'r') as file:
#         word_list = [line.strip().split(';') for line in file]
# else:
#     print(f"Error: File '{word_list_file}' not found.")
#     sys.exit(1)
# 
# # Convert scores to integers
# word_list = [(word, int(score)) for word, score in word_list]
# 
# # Create a set of all words for efficient lookup
# all_words_set = {re.sub(r'[^a-zA-Z]', '', word.lower()) for word, _ in word_list}
# 
# # Print the number of words in all_words
# print(f"Number of words in word_list: {len(word_list)}")
# print(f"Number of words in all_words_set: {len(all_words_set)}")
# 
# # Read word pairs to find
# if args.find_words:
#     find_list = read_find_words_from_string(args.find_words)
# else:
#     find_words_file_path = args.find_words_file
#     find_list = read_find_words_from_file(find_words_file_path)
# 
# # Call the check_words function with the provided lists and chosen comparison function
# found_words = check_words(find_list, word_list, lower_bound=70, similarity_threshold=0.5, comparison_func=comparison_func)
# 
# # Print the number of words in found_words
# print(f"Number of found words: {len(found_words)}")
# 
# # Sort the found_words list in descending order of score, then descending order of word length
# found_words.sort(key=lambda x: (x[3], -len(x[0])), reverse=True)
# 
# # Limit the number of words to be printed
# found_words = found_words[:2000]
# 
# # Print the found_words list
# for find_word1, find_word2, word, score in found_words:
#     print(f"Find Word 1: {find_word1}, Find Word 2: {find_word2}, Found Word: {word}, Score: {score}")
# 
# # Print the results in CSV format
# print("Printing results in CSV format:")
# with open("found_words.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Find Word 1", "Find Word 2", "Found Word", "Score"])
#     for find_word1, find_word2, word, score in found_words:
#         writer.writerow([find_word1, find_word2, word, score])
