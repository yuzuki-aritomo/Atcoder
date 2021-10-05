import io
import sys
_INPUT = """\
<>>
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
A = [0 for _ in range(len(S)+1)]

def solve(n):
  i = 0
  while(n+i < len(S)):
    if(S[n+i] == "<"):
      if(A[n+i+1] > i+1):
        break
      A[n+i+1] = i + 1
      i += 1
    else:
      break
  i = 1
  while(0 <= n-i):
    if(S[n-i] == ">"):
      if(A[n-i] >= i):
        break
      A[n-i] = i
      i += 1
    else:
      break

for i in range(len(S)-1):
  if(i == 0 and S[i] == "<"):
    A[i] = 0
    solve(i)
  elif(i == len(S)-2 and S[i+1] == ">"):
    A[i+2] = 0
    solve(i+2)
  elif(S[i] == ">" and S[i+1] == "<"):
    A[i+1] = 0
    solve(i+1)

if(len(S) == 1):
  solve(0)
  solve(1)


print(sum(A))