import io
import sys
_INPUT = """\
191
"""
sys.stdin = io.StringIO(_INPUT)

import math
N = int(input())
A = math.floor(N*1.08)


if(A == 206):
  print("so-so")
elif(A > 206):
  print(":(")
else:
  print("Yay!")