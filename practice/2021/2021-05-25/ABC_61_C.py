import io
import sys
_INPUT = """\
9999999999
"""
sys.stdin = io.StringIO(_INPUT)


S = input()
n = len(S)-1
from itertools import product

Ans = 0
for bits in product([0, 1], repeat=n):
    tmp = []
    j = 0
    for i in range(n):
        if(bits[i]):
            tmp.append(int(S[j:i+1]))
            j = i+1
    tmp.append(int(S[j:n+1]))
    Ans += sum(tmp)

print(Ans)