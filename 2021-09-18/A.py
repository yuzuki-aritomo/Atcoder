import io
import sys
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

if(N<40):
  print(40-N)
elif(N<70):
  print(70-N)
elif(N<90):
  print(90-N)
else:
  print("expert")

