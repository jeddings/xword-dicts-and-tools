import re
import sys
import argparse
import os

# Get the RegeEx pattern from the command line parameter. Prompt if missing.

parser = argparse.ArgumentParser(description='Search a dict file using a regex pattern. '
                                 'Supports $v (vowel) and $c (consonant) shorthands.')
parser.add_argument('pattern', nargs='?', help='Regex pattern to search for')
parser.add_argument('--dict-file', default=None,
                    help='Path to the .dict file to search (default: ../dictionaries/*.dict first match)')
args = parser.parse_args()

pattern = args.pattern if args.pattern else input("Enter RegEx: ")

if len(pattern) == 0:
    sys.exit()

# Compile the pattern into a RegEx Object so it only has to be evaluated once.

prog = re.compile(pattern.replace("$v", "[aeiou]").replace("$c", "[^aeiou]"), re.IGNORECASE)

if args.dict_file:
    dict_file = args.dict_file
else:
    import glob
    script_dir = os.path.dirname(os.path.abspath(__file__))
    matches = glob.glob(os.path.join(script_dir, "..", "dictionaries", "*.dict"))
    if not matches:
        print("Error: no .dict files found. Use --dict-file to specify one.")
        sys.exit(1)
    dict_file = matches[0]

with open(dict_file, "r") as f:
    lines = f.readlines()

i = 0

for line in lines:

    parts = line.split(';')
    word = parts[0]

    if prog.search(word):

        print(word)

        if i > 10000:
            break

        i += 1


        
