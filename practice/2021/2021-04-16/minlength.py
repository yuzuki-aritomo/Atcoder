import io
import sys
_INPUT = """\
4 4
0 s 0 1
1 0 0 0
0 1 1 1
0 0 0 g
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

N, M = map(int, input().split())
Map = []
for i in range(M):
    Map.append(list(map(str,input().split())))
for i in range(M):
    for j in range(N):
        if(Map[i][j] == "s"):
            Start = [i, j]
        elif(Map[i][j] == "g"):
            Goal = [i, j]

def bfs():
    X = [0, 1, 0, -1]
    Y = [-1, 0, 1, 0]
    path = [[0 for i in range(N)] for i in range(M)]
    Q = deque()
    Q.append(Start)
    while(len(Q) != 0):
        tmp = Q.popleft()
        I = tmp[0]
        J = tmp[1]
        for k in range(4):
            i = I + X[k]
            j = J + Y[k]
            if(i >=0 and i<M and j>=0 and j<N):
                if(Map[i][j] == "0"):
                    Map[i][j] = "@"
                    path[i][j] += (path[I][J] + 1)
                    Q.append([i, j])
                elif(Map[i][j] == "g"):
                    print(path[I][J] + 1)
                    exit()
    print("Fail")

bfs()