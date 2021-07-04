import io
import sys
_INPUT = """\
100 600

"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

if(A<= B and B<= A*6):
  print("Yes")
else:
  print("No")