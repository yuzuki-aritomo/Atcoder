import io
import sys
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
"""
sys.stdin = io.StringIO(_INPUT)


from collections import deque
from collections import Counter

N = int(input())
M = [[] for i in range(N+1)]
C = list(map(int,input().split()))
C.insert(0, 0)
for i in range(1,N):
    a, b = map(int, input().split())
    M[a].append(b)
    M[b].append(a)

def dfs():
    Ans = [0 for i in range(N+1)]
    color = [0 for i in range(N+1)]
    parent = [0 for i in range(N+1)]
    depth = 0
    Q = deque()
    Ans[1] = 1
    color[1] = 1
    Q.append(1)
    while(len(Q)!=0):
        depth += 1
        u = Q.popleft()
        for item in M[u]:
            if(color[item] == 0):
                Q.append(item)
                color[item] = 1
                Flag = False
                parent[item] = u
                pa = parent[item]
                for j in range(depth):
                    if(C[pa] == C[item]):
                        Flag = True
                        break
                    pa = parent[pa]
                if(Flag): break
                Ans[item]  = 1
    for i in range(1, N+1):
        if(Ans[i] == 1):
            print(i)
dfs()