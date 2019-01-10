def fibonacci(n,k):
    if n == 0:
            return 0
    if n == 1:
        return 1
    else:
        return (fibonacci(n-1, k) + k * fibonacci(n-2, k))


print (fibonacci(35,4))