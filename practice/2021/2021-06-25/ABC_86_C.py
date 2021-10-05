import io
import sys
_INPUT = """\
2
5 1 1
100 1 1

"""
sys.stdin = io.StringIO(_INPUT)


def solve(A, B):
  t = B[0] - A[0]
  x = abs(A[1] - B[1])
  y = abs(A[2] - B[2])
  if(t >= x + y):
    if((t-(x+y))%2 == 0):
      return True
  return False


N = int(input())
A = []
for i in range(N):
  A.append(list(map(int,input().split())))

if(not solve([0, 0, 0], A[0])):
  print("No")
  exit()
for i in range(N-1):
  if(not solve(A[i], A[i+1])):
    print("No")
    exit()
print("Yes")