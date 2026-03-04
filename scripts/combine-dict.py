#!/usr/bin/python3

import re
import sys

# Get the name of the output file
output_file_name = sys.argv[1]

# Check if the output file exists
try:
  open(output_file_name, "r")
except FileNotFoundError:
  # The file does not exist, so create it
  with open(output_file_name, "w") as f:
    f.write("")

# Read the lines from stdin
try:
  lines = input().splitlines()
except EOFError:
  print("No input")
  exit()

# Loop over the lines
for line in lines:
  print(line)
  
  # Strip out any non-alpha characters from the word
  word = re.sub("[^a-zA-Z]", "", line)

  # Lowercase the word
  word = word.lower()
#   print(word)
  
  # Check if the word is already in the output file
  if word not in open(output_file_name, "r").read():

    # Write the word to the output file
    with open(output_file_name, "a") as f:
      f.write(word + "\n")
