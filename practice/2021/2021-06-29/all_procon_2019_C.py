import io
import sys
_INPUT = """\
314159265 35897932 384626433

"""
sys.stdin = io.StringIO(_INPUT)

K, A, B = map(int, input().split())

# 2 => -A + B
#1 => continue

if(B>A+1 and K > A):
  k = K - (A - 1) #5
  if(k%2 == 0):
    print(k//2*(B-A) + A)
  else:
    print(k//2*(B-A) + 1 + A)
else:
  print(K+1)