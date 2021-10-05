import io
import sys
_INPUT = """\
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3
"""
sys.stdin = io.StringIO(_INPUT)

import copy

N, M, Q = map(int, input().split())

A = [[] for i in range(51)]
for i in range(N):
    # A.append(list(map(int,input().split())))
    a,b = map(int, input().split())
    for i in range(a, 51):
        A[i].append(b)
X = list(map(int,input().split()))
print(A)

print("A:", A)
print("X:", X)

def solve(L, R):
    Goods = copy.deepcopy(A)
    BOX = copy.deepcopy(X)
    del BOX[(L-1):R]
    BOX.sort()
    print(L, R)
    print(BOX)
    ans = 0
    for i in range(1,len(BOX)):
        tmp = max(A[Goods[i]])
        tmp_in = A[Goods[i]].index(tmp)
        for k in range(Goods[i], 51):
            Goods[k].pop(tmp_in)
        ans += tmp
    print(ans)


for i in range(Q):
    L, R = map(int, input().split())
    solve(L, R)