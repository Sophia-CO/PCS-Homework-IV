n = 3
data = [line.strip() for line in open('INSERT DIRECTORY\rosalind_grph.txt')]
i = 2
while i < len(data):
    if not data[i].startswith('>') and not data[i-1].startswith('>'):
        data[i-1] += data[i]
        del data[i]
        i -= 1
    i += 1
dataset = {}
for i in range(0,len(data),2):
    dataset[data[i][1:]] = data[i+1]
for first in dataset.keys():
    for second in dataset.keys():
        if first != second and dataset[first][len(dataset[first])-n:] == dataset[second][0:n]:
            print (first + " " + second)