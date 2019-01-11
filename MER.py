from __future__ import print_function, division
import os
def mergeARR(A, B):
    a1 = len(A)
    b1 = len(B)
    i = j = 0
    AB = []
    while i < a1 and j < b1:
        if A[i] < B[j]:
            AB.append(A[i])
            i += 1
        else:
            AB.append(B[j])
            j += 1
    if i < a1:
        AB += A[i:]
    elif j < b1:
        AB += B[j:]
    return AB
if __name__ == "__main__":
    with open(os.path.join('INSERT DIRECTORY \rosalind_mer.txt')) as dataset:
        dataset.readline()
        A = [int(r) for r in dataset.readline().strip().split()]
        dataset.readline()
        B = [int(r) for r in dataset.readline().strip().split()]
        print(*mergeARR(A, B))
