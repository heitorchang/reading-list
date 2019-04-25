import os

DIRECTORY = "c:/Users/Heitor/Desktop/code/reading-list/duolingo_chinese/"

FILE = "vocab_cedict.txt"

os.chdir(DIRECTORY)

with open(FILE, encoding="utf8") as infile:
    for line in infile:
        line = line.strip()
        if 1 <= len(line) <= 6:
            print(line)
