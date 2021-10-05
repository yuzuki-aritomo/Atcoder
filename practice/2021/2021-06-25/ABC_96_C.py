import io
import sys
_INPUT = """\
5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#
"""
sys.stdin = io.StringIO(_INPUT)


H, W = map(int, input().split())

M = []
for i in range(H):
  M.append(input())

def check(i, j):
  path_X = [0, -1, 0, 1]
  path_Y = [-1, 0, 1, 0]
  for k in range(4):
    x = i + path_X[k]
    y = j + path_Y[k]
    if(0 <= x and x < H and 0<=y and y<W):
      if(M[x][y] == "#"):
        return True
  return False


for i in range(H):
  for j in range(W):
    if(M[i][j] == "#"):
      #上下左右
      if(not check(i, j)):
        print("No")
        exit()
print("Yes")
