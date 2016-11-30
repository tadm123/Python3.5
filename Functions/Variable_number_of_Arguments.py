# http://www.learnpython.org/en/Multiple_Function_Arguments

# Function with variable arguments

def foo(first, second, third, *num):   #*num is a tuple of the rest
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(num))

foo('Daniel','George','Tom','Michael','Jim','John')



def foo(*num):          #This is a tuple
    for i in num:
        print('Hello '+ num)

foo('Daniel','George','Tom','Michael','Jim')


