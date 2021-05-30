import io
import sys
_INPUT = """\
3 2
1 7 0
5 8 11
10 4 2
"""
sys.stdin = io.StringIO(_INPUT)

import math
N, K = map(int, input().split())

A = []
for i in range(N):
    tmp = list(map(int,input().split()))
    A.append(tmp)

List_R = []
List_L = []
for i in range(K):
    List_R.append(A[i][0:K])
    List_L.append(A[0:K][i])

print(List_R)
print(List_L)
