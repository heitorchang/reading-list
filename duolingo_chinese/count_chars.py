# Load vocab.txt and tally how many different characters are there.
# 749 characters in the middle of Travel 4 (77)

import os

DIRECTORY = "c:/Users/Heitor/Desktop/code/reading-list/duolingo_chinese/"

INFILE = "vocab.txt"


os.chdir(DIRECTORY)

s = set()

with open(INFILE, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0 or line[0].isdigit():
            continue
        for c in line:
            s.add(c)

print(s)

print(len(s))
