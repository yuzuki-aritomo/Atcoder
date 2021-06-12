import io
import sys
_INPUT = """\
0 0
"""
sys.stdin = io.StringIO(_INPUT)


a, b = map(int, input().split())

if(a == b):
  print(a)
elif(a != 0 and b != 0):
  print(0)
elif(a != 1 and b != 1):
  print(1)
elif(a != 2 and b != 2):
  print(2)