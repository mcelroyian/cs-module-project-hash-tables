import re

def word_count(s):
    # Your code here
    d = {}
    s_clean = re.sub(r'[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]', "", s)
    s_clean = re.sub(r'(\s)+', " ", s_clean).lower().strip()
    
    if not s or not s_clean:
        return d
    
    for s in s_clean.split(" "):
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
    return d

if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
    #print(word_count("Hello    hello"))
    #print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    #print(word_count('This is a test of the emergency broadcast network. This is only a test.'))