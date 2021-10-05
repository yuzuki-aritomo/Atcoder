import io
import sys
_INPUT = """\
4
1 2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
H = list(map(int,input().split()))

def Change(i, maxH):
  for j in range(i, N):
    if(H[j] == maxH):
      H[j] -= 1
    else:
      return

Ans = 0
while(True):
  maxH = max(H)
  if(maxH == 0):
    break
  for i in range(N):
    if(H[i] == maxH):
      Change(i, maxH)
      Ans += 1

print(Ans)