import io
import sys
_INPUT = """\
6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
M = []
for i in range(H):
  M.append(list(input()))

for i in range(H):
  for j in range(W):
    if(M[i][j] == "."):
      M[i][j] = 0

Path = [[-1, -1], [-1, 0],[-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(H):
  for j in range(W):
    if(M[i][j] == "#"):
      for p in Path:
        x = i + p[0]
        y = j + p[1]
        if(0 <= x and x<H and 0 <= y and y<W ):
          if(M[x][y] != "#"):
            M[x][y] += 1

for item in M:
  print("".join(map(str, item)))

