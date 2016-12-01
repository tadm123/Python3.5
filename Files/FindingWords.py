# ThinkPython - http://greenteapress.com/thinkpython2/html/thinkpython2010.html
# Project: Finding a word with three consecutive letters

import os

os.chdir('c:\\users\\patty\\desktop')

fp = open('allwords.txt')
words_list = fp.readlines()

for letter in words_list:
	let = letter.strip()
	for i in range(2,len(let)):
		if let[i] == let[i-1] == let[i-2]:
			print(let)

fp.close()

#Finding a word with three consecutive double letters (ex: mississippi, if there was a double 'i' it would qualify)
'''			
			
fp = open('allwords.txt')
words = fp.read()
regex = re.compile(r'[a-z]*([a-z])\1([a-z])\2([a-z])\3[a-z]*')
mo = regex.search(words)
mo.group()
fp.close()


'''
