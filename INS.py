def ins(n,A):
    swap_num = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            swap_num += 1
            k -= 1
    return swap_num
with open('INSERT DIRECTORY\rosalind_ins (1).txt') as f:
    i=0
    n=0
    a=[]
    for line in f:
        text=line.strip()
        if i==0:
            n=int(text)
        else:
            a=[int(t) for t in text.split(' ')]
        i+=1
    print (ins(n,a))