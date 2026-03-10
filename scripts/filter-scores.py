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

