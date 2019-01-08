def fib(n):

    a,b = 1,1

    for i in range(n-1):

        a,b = b, b+a

    return a

print (fib(24))
