def revc(c):
    compl = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([compl[c] for c in reversed(c)])
def revp(c):
    results = []
    l = len(c)
    for i in range(l):
        for j in range(3, 13): #inclusive of the length 4 and 12 string
            if i + j > l:
                continue
            s1 = c[i:i+j]
            s2 = revc(s1)
            if s1 == s2:
                results.append((i + 1, j))
    return results

if __name__ == "__main__":
    fasta = {}
    dna = "GCGCGTTATCCACGTGAAGGAAAATCGGACTTACGGTATTTAGACTTATCACTTCGTGTACATAACCCTATTCTGCCGCTTATGAAAATCGCACTAACTAAACCTGATGTCTTCTCTCACGATCGGCCAGGTGGCGGCAGTTGGGTGAGCTCAACGTAATGGGCAAGATGGTGGTAGTAAACAGATCGAAGTTTAGCCCTTCCAACAAAGTAGAAGGGTATAGTATCTTGGACTAGATATACTCCCGAAGTGGACATCGGAATCTAAGGCGACTATGGGTCTAGCGGATATGGGCGGACTAGCCCTACTACTAATTGGAGCACATCCGCATTCAGTTCGAAAGCACAAAAGCGTACTGAATGGGATACCAATGAATCTTTCGCGATCCCACCAAACAAGATTCCTCATGAGGAGCGCACTACGGCCTTAAACGTACGACTCCAGCAATGCTCGAATGGCAAGAGATGTGGGTTCATGGTCCCGGCAAGATCTCCGTTCGTGCTGATGCTCTGTAGTAAATCGGTAGGGAACCATTGTTCGTACATTGTACTTCATAATTCCCGAACGCGCTGGGTGTATTTGTATCCGTCACCTCCGTCCTGCAATTGCCTGGACGTATCGCCGGGGTTCTCCACTCGGCTCCTCAATTGAGTGTGTCACTGCTGGTATACTTTATGTTCGCTTTTCGCTATTAAACAGTTCCAGGTGAACACAATTGGTGTCCCCCCCTAACCCAGCCGACCGAGGAGTAGCGATTGAGAAGAATGAGAGGAATCTAGTGTAGATTGGAACATGGGAAAGGACCCTTCTGCGC"
    results = revp(dna)
    print("\n".join([' '.join(map(str, r)) for r in results]))