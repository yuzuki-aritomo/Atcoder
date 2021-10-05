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

N = int(input())
A = [[0 for i in range(N)] for j in range(N)]
color = [0 for i in range(N)]
start = [0 for i in range(N)]
finish = [0 for i in range(N)]

for i in range(N):
    B = list(map(int,input().split()))
    for k in range(B[1]):
        A[B[0]-1][B[k+2]-1] = 1

time = 0
def dfs(u):
    global time
    color[u] = 1
    time += 1
    start[u] = time
    for v in range(N):
        if(A[u][v]==1 and color[v]==0):
            dfs(v)
    color[u] = 2
    time += 1
    finish[u] = time

for i in range(N):
    if(color[i]==0):
        dfs(i)

for i in range(N):
    print(i+1,start[i],finish[i])