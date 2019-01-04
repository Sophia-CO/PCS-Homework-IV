n = 97
m = 20
g= [0 for i in range(m-1)] # start from the first int looking through the numbers
g.append(1)
for h in range(n-1):
    r = sum([g[i] for i in range(m-1)])
    for i in range(m-1):
        g[i] = g[i+1]
    g[m-1] = r
print (sum(g))