s = 'CAAACGTTTCTACCCCTGCCAAAGGGGACTCGCCTCGTATCGTATCGACTCCGTTCTCGACTCAGTAGGAACTACTAACAAGATTAAGTAAGGTTGAAAGATAGACCGTTATAATAGATAGTTCCTCCTTTACCCGATCGGCCTTTTGATCCTAGAGGAATCGACAGGGTAAGAAATGGTGGGGCACAAGGGGTCGAGGGTCTAATCGGGAATCATATGGGAGTTTCTCCATTTACCGGGGCGTGAGTTCGGAGAAATCTTATTGTCACTGGCCTACCTGATAGATCCAATTCATAGAGTATTGCTTTATGTCCAGAAGTAGTTTGTCTTGGGCGTGAGCGTGCTAGCCCAATACGTAGAGATTTTAGTCTAAGCGAGACGAGTGGCTGGACTAACCCGGTTAGCCTGTTGTTTGGGCGCGCATAGTTATCCTATACTTTCTTATACATAAGTCACAATTGAGCGTAGAAATGGATTTAGGAGTTAACCGATAGGATACTCGCAAACGTTGGAAAATGCCGCTGGAAAGATTCGCGGCAGGGATACAGAGTAATCCCACCCTCGTAGGGAAAGGCAATATGGTAGGTTCAGTTCTGCAGATGCATAACACAGTGTTCTTACTAGGACGGTTCTAGTCGGCACAGGCCCCGAGCTTAGGCTATGCGGGGACGTCGTCCCTGGGGCGTGTATGACAAATTCCAGTAATCGGCATCATAATGGCGGCCGACCGTGCGGAGGAATTGCATGTTTTTTATAGAGCGGCCTACTTCTGGCACAATTCTGAGTTGCTATGTCAAATTGCTCTTGGTGACAAAGTATTACTTCAGCATTCAAAGTACCACATCTGGGCGGGTTCCAATATGGAAGCGAGGCAGCCACCATAAGTGTATACTTTTCATGAACCCAGAGCCGTTCCTACCCCTCTGCGGTACAAGAAATAAAAAGCTCTCGTCACCGAATCTA'
t = 'GATACGTTCCTGACCCCGCCATAAGAAATGGGTTTGAGACCATATCCAATCCGGTCGTGTCGCAGTCCATACGACTAACTAGAATATGGGTTGTTAACTGACCCACCGGTATGTAAGGTGGGTCCACCTTTGCCGGATCAAACATCCCCTCATACAGGAATTGAACTTGATATCGATGCATCGGCAGTCCGGAAGCAGGGTCTTTCCGAGAATCCTGACGGAGCCGACCACTTTGCCGAATGGCCAGATTGACGCTCTCGTATGGTTCTGGGTCTCCCAGACCCAGCTCATTAGGCCGGAATGGGTTTGAATTCATTAGAAGGGGCTAGTGAAGCGCAGCGTACTTGACGGGTTAGTTAAACATCTGCTACATGCGAGACCAGTTCCTGGTGTGTACGTATTAGGCTCTTGTGTCCACGCAAATTTAGAGGCCTTTTCTCCGCACAAAAATGTCAGAGTTTCCCGTGCACTCGTAGCCGCAGATATTAAAATTTTACCTACCGGTTCATGGAAATGTTCCATTGGAATCAACCGATACAGGGATACCGTGTACTCTTACGCTGTTGGCGCAGTTATCAAAGCGAGGGTGAAGTCTCCAGTACCATGACGGATGGCTCCGGCGGGTACGGTTTGGCTCCTCAGTCGAATCTTTCTGCGGCTGGGCAGAGACAGGTTACATGAGGCTTATATCACGAATACTAGTATGTCCCCAGACCATATAGACCGACATTGTGAACGAAATAGCCATTATTGATCTGGCGGCTTAAATCGGGAGGAATTAGGTATATTGATTCAATATCACCCAGAATGAAGTAGAGCAAATCAGGGTGTTATTTGAAGGACTCTCTGAAATACGCAATGTATACTTGTTGTTCTGGCGTGGGGGCTCGACTTTGAATGAACCCGGCCCTGCTCTAAACAGCCTGTGCATCTCGTAACACCGATTTTGCGTTGCCTCCACGG'
count = 0  #starts counting from zero
for i in range(len(s)):
    if s[i] != t[i]:
        count += 1
print (count)