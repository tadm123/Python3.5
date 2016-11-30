# http://www.learnpython.org/en/Multiple_Function_Arguments

# It is possible to declare functions which receive a variable number
# of arguments, using the following syntax:

def foo(first, second, third, *therest):   #*therest is a tuple of the rest
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo('Daniel','George','Tom','Michael','Jim','John')

'''Output:

First: Daniel
Second: George
Third: Tom
And all the rest... ['Michael', 'Jim', 'John']
'''

def foo(*num):          #This is a tuple
    for i in num:
        print('Hello '+ num)

foo('Daniel','George','Tom','Michael','Jim')

'''Output:
Hello Daniel
Hello George
Hello Tom
Hello Michael
Hello Jim
'''
