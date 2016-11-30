# "Automate The Boring Stuff" Book
# CH 4 Project: Comma Code.
# Write a function tha takes a list value as an argument and returns a
# string with all items separated by a comma and a space and inserted before the
# last item.

def listToString(list):
    string = ''
    for i in range(len(list)):
        if list[i] == list[-1]:                         #if it's on the last element
            string = string + ' and '+ list[i]+ '.'
        else:
            string += list[i]
            string += ', '

    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
string= listToString2(spam)

print(string)

