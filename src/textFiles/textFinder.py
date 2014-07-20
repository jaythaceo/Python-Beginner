#!/usr/bin/env python

# Count the lines of text.
textFile = open('text.txt')
count = 0
# Count the characters in the file.
numLines = 0
numWords = 0
numChars = 0

for line in textFile:
    words = count
    words = line.split()
    numLines += 1
    numWords += len(words)
    numChars += len(line)

print(numLines)
print(numWords)
print(numChars)

textFile.close()
