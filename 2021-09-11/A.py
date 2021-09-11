import io
import sys
_INPUT = """\
7
ooooooo

"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
A = input()

if(A[n-1] == "o"):
  print("Yes")
else:
  print("No")