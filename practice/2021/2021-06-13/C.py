import io
import sys
_INPUT = """\
-8 6 3
"""
sys.stdin = io.StringIO(_INPUT)

A,B,C = map(int, input().split())

if(C >0):
  C = C%2+2
elif(C<0):
  C = C%2 - 2

if(A**C == B**C):
  print("=")
elif(A**C < B**C):
  print("<")
else:
  print(">")
