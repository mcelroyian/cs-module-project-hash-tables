import random, re

def add_key(key, value, dict):
    if key not in dict.keys():
        dict[key] = []
    dict[key].append(value)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    d = {"start": {}, "stop": {}, "all":{}}
    word_list = re.sub(r'(\n)', "", words).split(" ")
# TODO: analyze which words can follow other words
# Your code here
    for index, word in enumerate(word_list):
        if word and index < len(word_list) - 1:
            if word[:1] == word[:1].upper():
                add_key(word, word_list[index+1], d["start"])
            if word[-1] == "." or word[-1] == "?" or word[-1] == "!":
                add_key(word, word_list[index+1], d["stop"])
            add_key(word, word_list[index+1], d["all"])

# TODO: construct 5 random sentences
# Your code here
    for s in range(6):
        print(f"\n{s})", end=" ")
        build = True
        cur = random.choice(list(d["start"]))
        while build:
            print(cur, end=" ")
            cur = random.choice(d["all"][cur])
            if cur in d["stop"].keys():
                print(cur)
                build = False
        



