import io
import sys
_INPUT = """\
5
-1 2 3 1 -1
2 -1 -1 4 -1
3 -1 -1 1 1
1 4 1 -1 3
-1 -1 1 3 -1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
    tmp = list(map(int,input().split()))
    tmp = [float("inf") if value==-1 else value for value in tmp]
    A.append(tmp)

color = [0 for i in range(N)]
d = [float("inf") for i in range(N)]
p = [-1 for i in range(N)]
def prim():
    d[0] = 0
    p[0] = -1
    while(True):
        mincost = float("inf")
        for i in range(N):
            if(color[i] != 1 and d[i]<mincost):
                mincost = d[i]
                u = i
        if(mincost==float("inf")):
            break
        color[u] = 1
        for v in range(N):
            if(color[v]!=1):
                if(A[u][v]<d[v]):
                    d[v] = A[u][v]
                    p[v] = u

prim()
print(sum(d))
