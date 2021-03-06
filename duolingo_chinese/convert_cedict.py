import os
import re

DIRECTORY = "c:/Users/Heitor/Desktop/code/reading-list/duolingo_chinese/"

INFILE = "vocab.txt"
OUTFILE = "vocab_cedict.txt"

CEDICT = "c:/Users/Heitor/Desktop/code/natural-languages/chinese/gwoyeu-romatzyh-studies/cedict.txt"


os.chdir(DIRECTORY)

# Code by Greg Hewgill
# https://stackoverflow.com/questions/8200349/convert-numbered-pinyin-to-pinyin-with-tone-marks

PinyinToneMark = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}

def decode_pinyin_syl(s):
    s = s.lower()
    r = ""
    t = ""
    for c in s:
        if c >= 'a' and c <= 'z':
            t += c
        elif c == ':':
            assert t[-1] == 'u'
            t = t[:-1] + "\u00fc"
        else:
            if c >= '0' and c <= '5':
                tone = int(c) % 5
                if tone != 0:
                    m = re.search("[aoeiuv\u00fc]+", t)
                    if m is None:
                        t += c
                    elif len(m.group(0)) == 1:
                        t = t[:m.start(0)] + PinyinToneMark[tone][PinyinToneMark[0].index(m.group(0))] + t[m.end(0):]
                    else:
                        if 'a' in t:
                            t = t.replace("a", PinyinToneMark[tone][0])
                        elif 'o' in t:
                            t = t.replace("o", PinyinToneMark[tone][1])
                        elif 'e' in t:
                            t = t.replace("e", PinyinToneMark[tone][2])
                        elif t.endswith("ui"):
                            t = t.replace("i", PinyinToneMark[tone][3])
                        elif t.endswith("iu"):
                            t = t.replace("u", PinyinToneMark[tone][4])
                        else:
                            t += "!"
            r += t
            t = ""
    r += t
    return r

def decode_pinyin(py):
    return " ".join(map(decode_pinyin_syl, py.split()))

def extract_pinyin(line):
    pat = re.compile(r'(?P<trad>.+) (?P<simp>.+) \[(?P<py>.*?)\] /(?P<eng>.*)/$')

    try:
        m = pat.match(line)
        return {'trad': m.group("trad"),
                'simp': m.group("simp"),
                'py': [decode_pinyin(m.group("py"))],
                'eng': m.group("eng")}
                                    
    except TypeError:
        return {}

def setup_cedict():
    cedict_dict = {}

    # skip lines that say 'see OTHER WORD'
    see_pat = re.compile(r'.+ .+ \[.+\] /see .+\[.+\]')
    
    with open(CEDICT, encoding="utf-8") as cedict_file:
        for line in cedict_file:
            if see_pat.match(line):
                continue
            if 'surname' in line or 'variant' in line or 'morphine' in line:
                continue
            parts = line.split()
            extracted = extract_pinyin(line)
            if parts[1] in cedict_dict:
                if extracted['py'][0] not in cedict_dict[parts[1]]['py']:
                    cedict_dict[parts[1]]['py'].append(extracted['py'][0])
                cedict_dict[parts[1]]['eng'] += "//" + extracted['eng']
            else:
                cedict_dict[parts[1]] = extracted

    return cedict_dict


def convert_vocab():
    with open(INFILE, encoding="utf-8") as infile, open(OUTFILE, 'w', encoding="utf-8") as outfile:
        cedict_dict = setup_cedict()
        for line in infile:
            try:
                data = cedict_dict[line.strip()]
                print("{} [{}] {}".format(data['simp'], ", ".join(data['py']), data['eng']), file=outfile)
            except KeyError:
                print(line.strip(), file=outfile)
        
