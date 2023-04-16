import io
import sys
_INPUT = """\
2
1 1
1 0
1 0
1 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

A = []
B = []
for i in range(N):
  A.append(list(map(int,input().split())))

for i in range(N):
  B.append(list(map(int,input().split())))


def check(a, b):
  for i in range(N):
    for j in range(N):
      if a[i][j] == 0:
        continue
      if a[i][j] == 1 and 1 == b[i][j]:
        continue
      else:
        return False
  return True


def trans(A):
  C = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      C[j][N-1-i] = A[i][j]
  return C


for _ in range(4):
  if check(A, B):
    print("Yes")
    exit()
  A = trans(A)

print("No")

