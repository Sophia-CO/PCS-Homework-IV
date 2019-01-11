def hd(str1, str2):
    result = 0
    for i in range(0, len(str1)):
        if(str1[i] != str2[i]):
            result += 1
    return result
def fastareader(strFileName):
    l = []
    str = ''
    with open(strFileName) as f:
        for line in f:
            if ('>' in line):
                if (str != ''):
                    l.append(str)
                    str = ''
            else:
                str = str + line.strip()
        if (str != ''):
            l.append(str)
    return l
strings = fastareader("INSERT DIRECTORY \rosalind_pdst.txt")
ln = len(strings)
st = strings[0]
ln_string = len(st)
matrix = [[0 for x in range(ln)] for y in range(ln)]
for i in range(0, ln):
    for j in range(0, i):
        matrix[i][j] = hd(strings[i], strings[j])/ln_string
        matrix[j][i] = matrix[i][j]
f = open('INSERT DIRECTORY \rosalind_pdst.txt', 'w')
line = ""
for i in range(0, ln):
    for j in range(0, ln):
        line = line + str(matrix[i][j]) + '\t'
    f.write(line)
    f.write('\n')
    line = ""