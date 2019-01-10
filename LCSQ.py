f = open("INSERT DIRECTORY\rosalind_lcsq.txt", "r")
lcsq = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
lcsq = str1.split(">")
lcsq.remove("")
s,t = lcsq
st = [''] * (len(t) + 1)
for i in s:
    ts = st
    st = ['']
    for j, k in enumerate(t):
        if(i == k):
            st.append(ts[j] + i)
        else:
            st.append(max(ts[j+1], st[-1], key=len))
print (st[-1])