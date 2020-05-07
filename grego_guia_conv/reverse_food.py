if __name__ == "__main__":
    rev_lines = open("food_glossary_reversed.txt", encoding="utf-8").readlines()
    entries = {}
    
    for i in range(0, len(rev_lines), 3):
        entries[rev_lines[i+1]] = rev_lines[i]

    with open("food_glossary_pt_gr.txt", "w", encoding="utf-8") as out:
        for k in sorted(entries):
            print(k, end="", file=out)
            print(entries[k], end="", file=out)
            print(file=out)
