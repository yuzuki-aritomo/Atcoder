import io
import sys
from typing import Tuple
_INPUT = """\
5
.....
..#..
.###.
.....
.....
.....
.....
....#
...##
....#
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
B = []
for i in range(N):
  T = input()
  for j in range(N):
    if(T[j] == "#"):
      A.append([i, j])
for i in range(N):
  T = input()
  for j in range(N):
    if(T[j] == "#"):
      B.append([i,j])

def isSame():
  A.sort()
  x = B[0][0]-A[0][0]
  y = B[0][1]-A[0][1]
  for i in range(len(B)):
    if(A[i][0] + x == B[i][0] and A[i][1] + y == B[i][1]):
      continue
    else:
      return False
  return True

if(len(A) != len(B)):
  print("No")
  exit()

for i in range(4):
  # print(A)
  if isSame():
    print("Yes")
    exit()
  for i in range(len(A)):
    A[i][0], A[i][1] = A[i][1], A[i][0]
    A[i][0] = N - A[i][0]

print("No")
