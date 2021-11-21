import io
import sys
_INPUT = """\
20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10

"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int,input().split()))
A.insert(0, 0)

S = set()
S.add(X)
tmp = X
while(True):
  tmp = A[tmp]
  if tmp in S:
    break
  else:
    S.add(tmp)

print(len(S))