import io
import sys
_INPUT = """\
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = [[0]]
for i in range(n):
    tmp = list(map(int,input().split()))
    A.append(tmp[2:])

color = [0 for i in range(n+1)]
S = [0 for i in range(n+1)]
F = [0 for i in range(n+1)]

time = 0
def dfs(u):
    global time
    color[u] = 1
    time += 1
    S[u] = time
    for item in A[u]:
        if(color[item]==0):
            dfs(item)
    time += 1
    F[u] = time
    color[u] = 2

for i in range(1,n+1):
    if(color[i]==0):
        dfs(i)

for i in range(1,n+1):
    print(i, S[i],F[i])