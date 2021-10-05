import io
import sys
_INPUT = """\
17
1 3 5 2 3 2 5 1 3 4 3 5 7 9 10 3 4
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())

class Node:
  def __init__(self, id):
    self.id = id
    self.S = set()
    self.mi1 = float("inf")
    self.mi2 = float("inf")

M = [Node(i) for i in range(2*10**5+1)]
A = list(map(int,input().split()))

for i in range(N//2):
  if(A[i] != A[N-1-i]):
    a = min(A[i], A[N-1-i])
    b = max(A[i], A[N-1-i])
    M[a].S.add(b)
    if(M[a].mi2 > b):
      if(M[a].mi1 > b):
        M[a].mi1, M[a].mi2 = b, M[a].mi1
      else:
        M[a].mi2 = b

for i in range(N):
  print(M[i].S)
  print(M[i].mi1)
  print(M[i].mi2)

# print(M)

Ans = 0
for i in range(len(M)):
  if(len(M[i].S) != 0):
    Ans += 1
    tmp = M[i].mi1
    print(M[i].S)
    print(M[i].mi1)
    M[i].S.remove(tmp)
    M[tmp].S |= M[i].S
    if(M[tmp].mi2 > M[i].mi2):
      if(M[tmp].mi1 > M[i].mi2):
        M[tmp].mi1, M[tmp].mi2 = M[i].mi2, M[tmp].mi1
      else:
        M[tmp].mi2 = M[i].mi2

print(Ans)
