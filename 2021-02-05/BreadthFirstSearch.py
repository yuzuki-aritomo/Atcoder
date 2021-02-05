import io
import sys
_INPUT = """\
6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

N = int(input())
A = [0]
color = [0 for i in range(N+1)]
d = [float("inf") for i in range(N+1)]
Q = deque()

for i in range(N):
    B = list(map(int,input().split()))
    B.pop(0)
    B.pop(0)
    A.append(B)

Q.append(1)
d[1] = 0
while(len(Q)!=0):
    a = Q.popleft()
    color[a] = 1
    for item in A[a]:
        if(color[item] == 0):
            d[item] = d[a] + 1
            color[item] = 1
            Q.append(item)

for i in range(1,len(d)):
    if(d[i] == float("inf")):
        print(i, -1)
    else:
        print(i, d[i])