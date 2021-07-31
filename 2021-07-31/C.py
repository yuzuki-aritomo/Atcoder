import io
import sys
_INPUT = """\
8 6
17 39 67 2 45 35 22 24
82 76 82 82 71 70
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int,input().split())

A = list(set(map(int,input().split())))
B = list(set(map(int,input().split())))

A.sort()
B.sort()
import bisect

ans = float("inf")
for item in A:
  a = bisect.bisect_left(B, item)
  b = max(0, a-1)
  if(a == len(B)):
    a = len(B)-1
  ans = min(ans, abs(B[a] - item), abs(B[b] - item))
print(ans)
