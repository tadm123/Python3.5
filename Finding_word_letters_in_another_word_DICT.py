# Problem 12 from http://greenteapress.com/thinkpython2/html/thinkpython2011.html: 
# Two words “interlock” if taking alternating letters from each forms 
# a new word. For example, “shoe” and “cold” interlock to form “schooled”.    
# Solution using a Dictionary:

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def is_match(s,s1):                     #both arguments are dictionaries
    for key in sorted(s):
        if s.get(key,0) > s1.get(key,0):
            return False
    return True

print('Type a word:')
some_word = input()
s= histogram(some_word)
fp= open('allwords.txt')

for line in fp:                 
    word = line.strip()
    s1 = histogram(word)
    if is_match(s,s1):
        print(word)

fp.close()
