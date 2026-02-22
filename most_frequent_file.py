from pytz import common_timezones

common = []
with open("3000-common-words.txt", "r") as f:
    for line in f.readlines():
        common.append(line.strip())

valid = []
with open("wiki-100k.txt", "r") as f:
    for line in f.readlines():
        valid.append(line.strip())

uncommon = []
with open("wordle-word-bank.txt", "w")as f:
    with open("valid-wordle-words.txt", "r") as g:
        for line in g.readlines():
            if line[0] == "#":
                continue
            if len(line.strip()) == 5:
                if line.strip() in valid and line.strip() in common:
                    f.write(line)