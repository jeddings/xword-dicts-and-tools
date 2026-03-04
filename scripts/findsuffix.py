import sys
import re
import glob

# Get the suffix string from command line, or prompt if it's missing.

pattern = sys.argv[1] if len(sys.argv) > 1 else input("Enter suffix: ")

# Bail if we didn't get a search string.

patternLength = len(pattern)

if patternLength == 0:
    sys.exit()

# Open the text file in read-only mode.
# If it isn't in current directory, specify full path using forward slash ("/") not backslash.
outputList = []

path = "/Users/jeddings/Dropbox/Crosswords/Dictionaries/*.dict"
for filename in glob.glob(path):
    # with open("../../*.dict", "r") as f:

    with open(filename, "r") as f:
        lines = f.readlines()
    
    i = 0               # counter to prevent runaway results
    fullWordList = []   # list of all words (not including scores) from file

    for line in lines:

        parts = line.split(';')
        fullWord: str = parts[0]      # Get the first part of the line, the word before ";"
        try:
            score: int = int(parts[1])
        except ValueError:
            score = 0
        except IndexError:
            score = 0
        if score >= 40 and len(fullWord) >= 3:
            fullWordList.append(fullWord.lower()) # All words get added to list
    
        # If the word ends with our suffix, see if we have already encountered that word without the suffix.
        # Note, since the list is parsed only once, this program assumes that the list is in alphabetical
        # order. So, for example, PASS would precede PASSION.

    fullWordListUniq = list(set(fullWordList))
    
    for fullWord in fullWordListUniq:
    
        if pattern in fullWord:

##        truncatedWord = fullWord.translate(str.maketrans('', '', pattern))
            truncatedWord = fullWord.replace(pattern, '')
        
            if truncatedWord in fullWordList:

                # print(truncatedWord + " : " + fullWord)
                outputList.append(truncatedWord + " : " + fullWord)
                
                if i > 10000:
                    break         # Limit to first 10000 words

                i += 1
outputListUniq = list(set(outputList))

outputListUniq.sort(key=len)

for pair in outputListUniq:
    print(pair)
    
