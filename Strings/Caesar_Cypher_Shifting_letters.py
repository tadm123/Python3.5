'''# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")'''

#http://stackoverflow.com/questions/419163/what-does-if-name-main-do    



def rotate_letter(letter, n):  #  letter= y, n = 3
    #Rotates a letter by n places
    if letter.isupper():
        start = ord('A')        #start = 65
    elif letter.islower():
        start = ord('a')        #start = 97
    else:
        return letter

    c = ord(letter) - start       #'y' - 'a' = 121 - 97 = 24
    i = (c + n) % 26 + start      #i = (24+ 3) % 26 = 1   +  97 = 98 = 'b'
    return chr(i)

def rotate_word(word,n):    #word = 'Hello there'
    new= ''
    for letter in word:
        new = new + rotate_letter(letter,n)
    return new



if __name__ == '__main__':         #This just means that this program is being run directly, it's all our
                                   #source code right here. It wasn't imported from another file into it.
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))

    
# So, code in this if block will only run if that module is the
# entry point to your program.

    








    










 
