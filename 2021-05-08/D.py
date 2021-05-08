import io
import sys
_INPUT = """\
3
2 3 202
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A = A[:8]
N = min(8, N)
Cnt = Counter()
Ans = {}
for bits in itertools.product([0, 1], repeat=N):
    tmp = 0
    for i in range(N):
        if(bits[i]):
            tmp += (A[i]%200)
    tmp %= 200
    if(Cnt[tmp] == 1):
        ans = bits
        Ans_1 = []
        Ans_2 = []
        for i in range(N):
            if ans[i]:
                Ans_1.append(i+1)
            if(Ans[tmp][i]):
                Ans_2.append(i+1)
        print("Yes")
        print(len(Ans_1), " ".join(map(str, Ans_1)))
        print(len(Ans_2), " ".join(map(str, Ans_2)))
        exit()
    Cnt[tmp] = 1
    Ans[tmp] = bits

print("No")