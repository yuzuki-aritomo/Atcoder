import io
import sys
_INPUT = """\
10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
A = []
for i in range(N):
  a, b = map(int, input().split())
  A.append((a, b))


A.sort(reverse=True)
ans = 0
i = 0
while W>0:
  if i > len(A)-1:
    break
  v = A[i][0]
  w = A[i][1]
  if W > w:
    ans += w*v
    W -= w
  else:
    ans += W*v
    break
  i+= 1

# print(A)
print(ans)