import io
import sys
_INPUT = """\
100
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

if 'o' in S and not ('x' in S):
  print('Yes')
else:
  print("No")

