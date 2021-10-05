import io
import sys
_INPUT = """\
77 42 36

"""
sys.stdin = io.StringIO(_INPUT)

a, B, C = map(int, input().split())

#A: 7 14 21 28
#B: 2 4 1 3
#C: 
A = a
M = [A%B]
while(True):
  A += a
  if(A%B == C):
    print("YES")
    exit()
  for item in M:
    if(A%B ==item):
      print("NO")
      exit()
  M.append(A%B)
