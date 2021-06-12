import io
import sys
_INPUT = """\
3
334 1000
334 1000
334 1000

"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
M = []
for i in range(N):
  M.append(list(map(int,input().split())))

M = sorted(M, key=lambda x: x[1])
T = 0
for i in range(N):
  T += M[i][0]
  if(T>M[i][1]):
    print("No")
    exit()

print("Yes")

