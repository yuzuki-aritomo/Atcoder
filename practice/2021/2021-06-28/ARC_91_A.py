import io
import sys
_INPUT = """\
1 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

if(N>2 and M>2):
  print(max(0,(N-2)*(M-2)))
else:
  if(N==1 and M== 1):
    print(1)
  elif(N == 1):
    print(max(0,M-2))
  elif(M == 1):
    print(max(0,N-2))
  else:
    print(0)