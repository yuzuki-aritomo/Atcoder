import io
import sys
_INPUT = """\
3 2
0 1 0
"""
sys.stdin = io.StringIO(_INPUT)

import collections

Cnt = collections.Counter

N, M = map(int, input().split())
A = list(map(int,input().split()))

Ans = N
cnt = Cnt(A[:M])
min_tmp = N

for i in range(N):
    if(cnt[i]==0):
        Ans = i
        min_tmp = i
        break

for i in range(N-M):
    cnt[A[i]] -= 1
    cnt[A[i+M]] += 1
    if(cnt[A[i]]==0 and A[i]<min_tmp):
        min_tmp = A[i]
        Ans = min(Ans, min_tmp)

print(Ans)