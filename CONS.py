def cons(dna):
    profile = [[0 for i in range(len(dna[0]))] for i in range(4)]
    for seq in dna:
        for i in range(len(seq)):
            if seq[i] == 'A':
                profile[0][i] += 1
            elif seq[i] == 'C':
                profile[1][i] += 1
            elif seq[i] == 'G':
                profile[2][i] += 1
            elif seq[i] == 'T':
                profile[3][i] += 1
    return profile

def consensus(profile):
    c = ''
    for i in range(len(profile[0])):
        m = max([profile[j][i] for j in range(4)])
        if profile[0][i] == m:
            c += 'A'
        elif profile[1][i] == m:
            c += 'C'
        elif profile[2][i] == m:
            c += 'G'
        elif profile[3][i] == m:
            c += 'T'
    return c
dataset = [line.strip() for line in open('insert directory')] #CHANGE USING YOUR DIRECTORY
n = 2
while n < len(dataset):
    if not dataset[n].startswith('>') and not dataset[n-1].startswith('>'):
        dataset[n-1] += dataset[n]
        del dataset[n]
        n -= 1
    n += 1
profile = cons([dataset[i] for i in range(1,len(dataset),2)])
print (consensus(profile))
print ('A: ' + str(profile[0])[1:].replace(']','').replace(',',''))
print ('C: ' + str(profile[1])[1:].replace(']','').replace(',',''))
print ('G: ' + str(profile[2])[1:].replace(']','').replace(',',''))
print ('T: ' + str(profile[3])[1:].replace(']','').replace(',',''))