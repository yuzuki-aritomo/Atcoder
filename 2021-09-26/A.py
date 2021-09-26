import io
import sys
_INPUT = """\
630 940 314
"""
sys.stdin = io.StringIO(_INPUT)


a, b, c = map(int, input().split())

if(a%c == 0):
  tmp = a//c
else:
  tmp = a//c + 1

if(tmp*c<=b):
  print(tmp*c)
else:
  print(-1)

