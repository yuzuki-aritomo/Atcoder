import io
import sys
_INPUT = """\
1233
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

i, j, n, m = int(S[0]), int(S[1]), int(S[2]),int(S[3])

if(S[0] == S[1] and S[1] == S[2] and S[2] == S[3]):
  print("Weak")
  exit()

tmp = i+1
if(tmp == 10):
  tmp = 0
if(tmp == j):
  tmp += 1
  if(tmp == 10):
    tmp = 0
  if(tmp == n):
    tmp += 1
    if(tmp == 10):
      tmp = 0
    if(tmp == m):
      print("Weak")
      exit()
print("Strong")
