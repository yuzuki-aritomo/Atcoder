import io
import sys
_INPUT = """\
2
3
1 2
2 3
3 3
5
1 2
2 3
3 3
1 3
999999999 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

from collections import defaultdict
from collections import Counter

def solve():
  N = int(input())
  A = Counter()
  B = Counter()
  for i in range(N):
    a, b = map(int, input().split())
    A[a] += 1
    B[b] += 1
  print(A)
  print(B)
  Ak = list(A.keys())
  Bk = list(B.keys())
  Ak.sort()
  Bk.sort()
  import bisect
  # Ans = [A[Ak[0]]-1]
  # for i in range(N):
  #   Ans.append(min(0, Ans[i-1]-(Ak[i] - Ak[i-1])) + A[Ak[i]])
  s = 0
  Ans = [1]
  h = 0
  for i in range(len(Ak)):
    h += A[Ak[i]]
    tmp = min(Ak[i] - Ak[i-1], h)
    h -= tmp
    s += tmp
    Ans.append(s)
  for i in range(len(Bk)):
    id = bisect.bisect_left(Ak, Bk[i])
    if(len(Ak) == id):
      id -=1
    if(Bk[i]-Ak[id]+Ans[id]>B[Bk[i]]):
      return False
  return True


T = int(input())
for i in range(T):
  if(solve()):
    print("Yes")
  else:
    print("No")
