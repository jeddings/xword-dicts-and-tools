import re
import sys

# Get the RegeEx pattern from the command line parameter. Prompt if missing.

pattern = sys.argv[1] if len(sys.argv) > 1 else input("Enter RegEx: ")

if len(pattern) == 0:
    sys.exit()

# Compile the pattern into a RegEx Object so it only has to be evaluated once.

prog = re.compile(pattern.replace("$v", "[aeiou]").replace("$c", "[^aeiou]"), re.IGNORECASE)

with open("../../XwiWordList 12-12-2020 cleaned.dict", "r") as f:
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


        
