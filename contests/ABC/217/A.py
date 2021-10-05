import io
import sys
_INPUT = """\
a aa


"""
sys.stdin = io.StringIO(_INPUT)

a,b = map(str, input().split())

if(a<b):
  print("Yes")
else:
  print("No")