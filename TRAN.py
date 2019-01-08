from Bio import SeqIO
f = open("insert file.txt", 'r')
raw_data = list(SeqIO.parse(f, "fasta"))
f.close()
seq1 = raw_data[0].seq
seq2 = raw_data[1].seq
transition = 0
transversion = float(0)
for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        continue
    elif seq1[i] == "A" and (seq2[i] == "C" or seq2[i] == "T"):
        transversion += 1
    elif seq1[i] == "G" and (seq2[i] == "C" or seq2[i] == "T"):
        transversion += 1
    elif seq1[i] == "C" and (seq2[i] == "A" or seq2[i] == "G"):
        transversion += 1
    elif seq1[i] == "T" and (seq2[i] == "A" or seq2[i] == "G"):
        transversion += 1
    else:
        transition += 1
print (transition/transversion)