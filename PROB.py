from math import log10
def prob(dna, array):
    array = map(float, array.split())# Calculate probability of DNA happening randomly
    random = []
    for i in array:
        chancedna = 1.0
        g = i * 0.5
        a = (1 - (g * 2)) * 0.5
        for j in dna:
            if j == "A":
                chancedna *= a
            if j == "T":
                chancedna *= a
            if j == "G":
                chancedna *= g
            if j == "C":
                chancedna *= g
        random.append(log10(chancedna))
    return " ".join(map(str, random))
def gc(dna):
    g = 0.0
    for k in dna:
        if k == "G":
            g += 1.0
        if k == "C":
            g += 1.0
    g = g / len(dna)
    return g
print(prob("TAAAATCGCATTGTGGAATGTCGTTGGACCAAAGTCAGACTAACCGACGAGGAATCACGAGATCCGGATCACCATAGACAGTATGTACATCTGCTCGTC","0.060 0.161 0.219 0.228 0.304 0.367 0.398 0.471 0.506 0.570 0.625 0.694 0.764 0.813 0.852 0.924"))