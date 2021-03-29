import io
import sys
_INPUT = """\
10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X.......
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque
from copy import deepcopy

def dfs(Sx, Sy, Goal):
    global H, W
    path = deepcopy(Map)
    color = deepcopy(Map)
    Q = deque()
    toX = [ 0, 1, 0,-1]
    toY = [-1, 0, 1, 0]
    path[Sx][Sy] = 0
    color[Sx][Sy] = 'X'
    Q.append([Sx, Sy])
    while(len(Q)!=0):
        u = Q.popleft()
        for i in range(4):
            x = u[0] + toX[i]
            y = u[1] + toY[i]
            #Mapを超えないかのチェック
            if(x>=0 and x<H and y>=0 and y<W):
                if(color[x][y]!='X'):
                    Q.append([x, y])
                    path[x][y] = path[u[0]][u[1]] + 1
                    if(color[x][y] == Goal):
                        return [x, y, path[x][y]]
                    color[x][y] = 'X'

H, W, N = map(int, input().split())
Map = []
for i in range(H):
    tmp = list(input())
    if("S" in tmp): S = [i, tmp.index("S")]
    Map.append(tmp)

Ans = 0
Re = dfs(S[0], S[1], '1')
Ans += Re[2]
for i in range(2, N+1):
    Re = dfs(Re[0], Re[1], str(i))
    Ans += Re[2]
print(Ans)