
def lcsm(dataset):
    for k in range(len(dataset[0]),1,-1):
        for start in range(len(dataset[0])-k+1):
            ds = dataset[0][start:start+k]
            found = True
            for i in range(1,len(dataset)):
                if not ds in dataset[i]:
                    found = False
                    break
            if found:
                return ds
dataset = [line.strip() for line in open('inser directory'[1])] #change using your directory 'worked with the text file
st = 2
while st < len(dataset):
    if not dataset[st].startswith('>') and not dataset[st-1].startswith('>'):
        dataset[st-1] += dataset[st]
        del dataset[st]
        st -= 1
    st += 1
st = 0
while st < len(dataset):
    del dataset[st]
    st += 1
print (lcsm(dataset))