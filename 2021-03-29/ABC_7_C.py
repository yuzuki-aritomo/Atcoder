import io
import sys
_INPUT = """\
5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque
from copy import deepcopy

def minus1(w):
    return int(w)-1

R, C = map(int, input().split())
Sx, Sy = map(minus1, input().split())
Gx, Gy = map(minus1, input().split())
Map = []
for i in range(R):
    Map.append(list(input()))

def dfs(Sx, Sy, Gx, Gy):
    global R, C
    path = deepcopy(Map)
    toX = [ 0, 1, 0,-1]
    toY = [-1, 0, 1, 0]
    path[Sx][Sy] = 0
    Q = deque()
    Q.append([Sx, Sy])
    while(len(Q)!=0):
        u = Q.popleft()
        for i in range(4):
            X = u[0]+toX[i]
            Y = u[1]+toY[i]
            #Map外にならないかチェック
            if(X>=0 and X<R and Y>=0 and Y<C):
                if(Map[X][Y]=="."):
                    path[X][Y] = path[u[0]][u[1]] + 1
                    Map[X][Y] = "#"
                    Q.append([X,Y])
        if(Map[Gx][Gy]!="."):
            print(path[Gx][Gy])
            break

dfs(Sx, Sy, Gx, Gy)