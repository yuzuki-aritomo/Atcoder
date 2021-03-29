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
M = [[] for i in range(N+1)]
for i in range(1,N+1):
    A = list(map(int,input().split()))
    for j in range(A[1]):
        M[i].append(A[j+2])

def dfs():
    color = [0 for i in range(N+1)]
    path = [-1 for i in range(N+1)]
    Q = deque()
    color[1] = 1
    path[1] = 0
    Q.append(1)
    while(len(Q)!=0):
        u = Q.popleft()
        for item in M[u]:
            if(color[item] == 0):
                Q.append(item)
                color[item] = 1
                path[item] = path[u] + 1
    for i in range(1, N+1):
        print(i, path[i])
dfs()

