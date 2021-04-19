import io
import sys
_INPUT = """\
4 4 2 2
##..
...#
#.#.
.#.#
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

H, W, X, Y = map(int, input().split())
Map = ["#" * (W+2)]
for i in range(H):
    Map.append("#"+ input() + "#")
Map.append("#" * (W+2))

Ans = 0
def dfs(x, y, a, b):
    global Ans
    if(Map[x+a][y+b] == "#"):
        return
    else:
        Ans += 1
        dfs(x+a, y+b, a, b)
dfs(X, Y, 0, -1)
dfs(X, Y, 1, 0)
dfs(X, Y, 0, 1)
dfs(X, Y, -1, 0)
print(Ans + 1)

