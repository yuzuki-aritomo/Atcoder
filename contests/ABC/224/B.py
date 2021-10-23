import io
import sys
_INPUT = """\
2 4
4 3 2 1
5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
M = []
for i in range(H):
  M.append(list(map(int,input().split())))

for i0 in range(H):
  for j0 in range(W):
    for i1 in range(i0+1, H):
      for j1 in range(j0+1, W):
        if not(M[i0][j0]+M[i1][j1]<=M[i1][j0]+M[i0][j1]):
          print("No")
          exit()

print("Yes")
