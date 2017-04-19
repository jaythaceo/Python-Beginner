#!/usr/bin

# Open file
f = open("mbox.txt", "r")

# Read file and print file
reader = f.read()
print(reader)

# Close file
f.close()