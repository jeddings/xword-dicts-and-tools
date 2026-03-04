import sys
import glob
import os

# Function to adjust scores based on the maximum score in the file
def adjust_scores(max_score, score):
    adjusted_score = score + (80 - max_score)
    return adjusted_score

# Function to process a file and extract word-score pairs
def process_file(file_path):
    words = set()
    scores = {}
    max_score = 0

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Split the line using ';' as a delimiter
            parts = line.split(';')

            # Skip lines that do not have exactly two parts
            if len(parts) != 2:
                continue

            try:
                word, score = parts[0].strip(), int(parts[1].strip())
                word = word.lower().strip()
                word = ''.join(c for c in word if c.isalpha() or c.isspace())

                # Ignore words that are below the score threshold
                if score < score_threshold:
                    continue

                # Find the maximum score in the file
                if score > max_score:
                    max_score = score

                # Add word-score pairs to the set and dictionary
                if len(word) >= min_length and len(word) <= max_length:
                    adjusted_score = score
                    if max_score < 80:
                        adjusted_score = score + (80 - max_score)
                    if word not in words or adjusted_score > scores[word]:
                        words.add(word)
                        scores[word] = adjusted_score

            except ValueError:
                # Handle invalid score values that cannot be cast to int
                print(f"Ignoring line due to invalid score: {line}")

#     return words, scores
    return scores

# # Function to process a file and extract word-score pairs
# def process_file(file_path):
#     scores = {}
# 
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
# 
#     for line in lines:
#         line = line.strip()
#         parts = line.split(';')
#         if len(parts) != 2:
#             continue
# 
#         word, score_str = parts[0].strip(), parts[1].strip()
#         try:
#             score = int(score_str)
#         except ValueError:
#             continue
# 
#         word = ''.join(c.lower() for c in word if c.isalpha() or c.isspace())
#         if len(word) >= min_length and len(word) <= max_length and score >= score_threshold:
#             scores[word] = max(score, scores.get(word, 0))
# 
#     return scores

# Function to write the word-score pairs to the output file
def write_results(output_file, scores):
    with open(output_file, 'w') as file:
        for word, score in sorted(scores.items()):
            file.write(f"{word};{score}\n")

# Main script
if __name__ == "__main__":
    # Check the command line arguments
    if len(sys.argv) != 3:
        print("Usage: python filter-scores.py <input_directory> <output_filename>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]
    filename_pattern = "*.dict"  # Filename pattern to match in the input directory
    score_threshold = 50
    min_length = 3
    max_length = 25

    total_scores = {}

    # Get the list of files matching the filename pattern in the input directory
    file_list = glob.glob(os.path.join(input_directory, filename_pattern))
    if not file_list:
        print("No files found matching the specified pattern in the directory.")
        sys.exit(1)

    # Process each file
    for file_path in file_list:
        scores = process_file(file_path)
        total_scores.update(scores)

    # Write the word-score pairs to the output file
    write_results(output_file, total_scores)

    # Print the summary information
    print("Total number of files processed:", len(file_list))
    print("Total number of words:", len(total_scores))
    print("Number of words outputted:", len(total_scores))


# import sys
# import os
# 
# # Function to adjust scores based on the maximum score in the file
# def adjust_scores(max_score, score):
#     adjusted_score = score + (80 - max_score)
#     return adjusted_score
# 
# # Function to process a file and extract word-score pairs
# def process_file(file_path):
#     words = set()
#     scores = {}
#     max_score = 0
# 
#     # Read the file line by line
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             # Split the line using ';' as a delimiter
#             parts = line.split(';')
#             if len(parts) != 2:
#                 continue
# 
#             word, score = parts[0].strip(), int(parts[1].strip())
#             word = word.lower().strip()
#             word = ''.join(c for c in word if c.isalpha() or c.isspace())
# 
#             # Ignore words that are below the score threshold
#             if score < score_threshold:
#                 continue
# 
#             # Adjust scores based on the maximum score in the file
#             if max_score < score:
#                 max_score = score
#             adjusted_score = adjust_scores(max_score, score)
# 
#             # Add word-score pairs to the set and dictionary
#             if len(word) >= min_length and len(word) <= max_length:
#                 if word not in words or adjusted_score > scores[word]:
#                     words.add(word)
#                     scores[word] = adjusted_score
# 
#     return words, scores
# 
# # Function to write the word-score pairs to the output file
# def write_results(output_file, words, scores):
#     with open(output_file, 'w') as file:
#         for word in sorted(words):
#             file.write(f"{word};{scores[word]}\n")
# 
# # Main script
# if __name__ == "__main__":
#     # Check the command line arguments
# 
#     if len(sys.argv) < 3:
#         print("Insufficient command-line arguments.")
#         print("Usage: python script.py <file_pattern> <output_file>")
#         sys.exit(1)
# 
#     file_pattern = sys.argv[1]
#     output_file = sys.argv[2]
#     score_threshold = 60
#     min_length = 8
#     max_length = 100
# 
#     total_words = set()
#     total_scores = {}
# 
#     # Process each file matching the input pattern
#     for file_name in os.listdir():
#         if file_name.endswith('.dict'):
#             words, scores = process_file(file_name)
#             total_words.update(words)
#             total_scores.update(scores)
# 
#     # Write the word-score pairs to the output file
#     write_results(output_file, total_words, total_scores)
# 
#     # Print the summary information
#     print("Total number of words:", len(total_words))
#     print("Number of words outputted:", len(total_scores))
#     print("Histogram of raw scores:")
#     print("Raw Score\tFrequency")
#     for score in total_scores.values():
#         print(score, "\t\t", total_scores.values().count(score))
#     print("Histogram of adjusted scores (written to the output file)")
