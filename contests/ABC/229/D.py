import io
import sys
_INPUT = """\
XXXX
200000
"""
sys.stdin = io.StringIO(_INPUT)

A = input()
K = int(input())
B = []
if(A[0]=="."):
  B.append(1)
else:
  B.append(0)
for i in range(1, len(A)):
  if(A[i]=="."):
    B.append(B[-1]+1)
  else:
    B.append(B[-1])


r = 0
l = 0
ans = 0
while(True):
  if(l == len(B)):
    break
  if(r < len(B) and (B[r] - B[l]) <= K):
    if((B[r] - B[l]) == K and A[l] == "."):
      ans = max(r - l, ans)
    else:
      ans = max(r - l+1, ans)
    r += 1
  else:
    l += 1


print(ans)