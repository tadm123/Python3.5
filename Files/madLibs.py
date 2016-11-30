# "Automate the Boring Stuff" Book
# CH8: Create a Mad Libs program that reads in text files and lets the user
# add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file

import re

text= ''''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.'''

i=0
Regex_A= re.compile(r'(ADJECTIVE)')
mo= Regex_A.findall(text)
for i in range(len(mo)):
        print('Enter an adjective:')
        adj= input()
        text= Regex_A.sub(adj,text,1)
        #text= text.replace("ADJECTIVE",adj,1)
        
i=0
Regex_N= re.compile(r'(NOUN)')
mo= Regex_N.findall(text)
for i in range(len(mo)):
        print('Enter an noun:')
        noun= input()
        text= Regex_N.sub(noun,text,1)
        #text= text.replace("NOUN",noun,1)

i=0
Regex_V= re.compile(r'(VERB)')
mo= Regex_V.findall(text)
for i in range(len(mo)):
        print('Enter a verb:')
        verb= input()
        text= Regex_V.sub(verb,text,1)        
        #text= text.replace("VERB",verb,1)
            

print(text)
	
#note it's better to use replace but I used regex.sub for practice.
#note that the format of re.sub is => re.sub(pattern, repl, string, count=0, flags=0)
#so if you only give a count of 1 it will replace only the first
