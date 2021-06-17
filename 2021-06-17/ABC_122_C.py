import io
import sys
_INPUT = """\
8 3
ACACTACG
3 7
2 3
1 8
"""
sys.stdin = io.StringIO(_INPUT)


import sys
def input():
  return sys.stdin.readline()[:-1]

N, Q = map(int, input().split())
S = input()
M = [0]*N
for i in range(N-1):
  if(S[i:i+2] == "AC"):
    M[i+1] = 1

for i in range(len(M)-1):
  M[i+1] = M[i] + M[i+1]

for i in range(Q):
  a, b = map(int, input().split())
  print(M[b-1] - M[a-1])







