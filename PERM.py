import itertools #creates iterators for easy looping
n = 5 
perms = list(itertools.permutations([i for i in range(1,n+1)]))
print (len(perms))
for p in perms:
    print (str(p)[1:].replace(')','').replace(',',''))
