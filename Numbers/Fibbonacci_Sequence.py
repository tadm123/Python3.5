#Writing a fibbonacci sequence

def fib(num):       #10
    n=[0,1]
    for i in range(2,num+1):        #from 2 index to 10
        n.append(n[i-1] + n[i-2])
    return n
        

fib(10)
#>>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#Doing it in recursive


def fibonacci(n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#Text says that don't try to reason his, your head will explode. Just
#trust in him with the 'leap of faith' theory
    
