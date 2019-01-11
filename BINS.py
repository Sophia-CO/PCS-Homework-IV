from __future__ import print_function, division
import os
import math
def binsearch(S,b):
    n = len(S)
    low = 0
    high = n - 1
    midD = math.floor(n / 2)
    prev = -1, -1, -1
    while (low, midD, high) != prev:
        prev = low, midD, high
        if b == S[low]:
            return low + 1
        elif b == S[high]:
            return high + 1
        elif b == S[midD]:
            return midD + 1
        elif b < S[midD]:
            high_i = midD
        elif b > S[midD]:
            low_i = midD
        midD = math.floor((high + low) / 2)
    return -1
if __name__ == "__main__":
    with open(os.path.join('INSERT DIRECTORY \rosalind_bins.txt')) as dataset:
        n = int(dataset.readline().strip())
        m = int(dataset.readline().strip())
        S = [int(r) for r in dataset.readline().strip().split()]
        query = [int(r) for r in dataset.readline().strip().split()]
        print(*[binsearch(S, b) for b in query])