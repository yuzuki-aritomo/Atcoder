import io
import sys
_INPUT = """\
100 2




"""
sys.stdin = io.StringIO(_INPUT)


a, b = map(int, input().split())

if(0<a and b==0):
  print("Gold")
elif(a==0 and 0<b):
  print("Silver")
elif(0<a and 0<b):
  print("Alloy")