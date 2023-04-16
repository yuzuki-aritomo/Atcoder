import io
import sys
_INPUT = """\
5
8
1 1 1
1 2 4
1 1 4
2 4
1 1 4
2 4
3 1
3 2
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
Q = int(input())

A = [set() for _ in range(N+1)] # iカードの箱
B = [[] for _ in range(N+1)] # i箱のカード

def com1(i,j):
  A[i].add(j)
  B[j].append(i)

def com2(i):
  print(sorted(A[i]))


def com3(i):
  print(sorted(B[i]))


for i in range(Q):
  c = list(map(int,input().split()))
  if c[0] == 1:
    com1(c[1], c[2])
  elif c[1] == 2:
    com2(c[1])
  else:
    com3(c[1])


