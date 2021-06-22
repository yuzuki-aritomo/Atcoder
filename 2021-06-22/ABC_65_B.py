import io
import sys
_INPUT = """\
5
3
3
4
2
4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Path = [0 for _ in range(N)]
A = []
for i in range(N):
  A.append(int(input()))

tmp = 0
i = 0
while(True):
  if(Path[tmp] == 1):
    print(-1)
    break
  if(tmp == 1):
    print(i)
    break
  Path[tmp] = 1
  tmp = A[tmp]-1
  i += 1