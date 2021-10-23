import io
import sys
_INPUT = """\
tourist
"""
sys.stdin = io.StringIO(_INPUT)


S = input()

if(S[-2]+S[-1] == 'er'):
  print("er")
else:
  print("ist")