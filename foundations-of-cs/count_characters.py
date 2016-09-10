# p. 13 The C Data Model

import sys

def main():
    num = 0
    while sys.stdin.read(1) != '\n':
        num += 1
    print(num)
