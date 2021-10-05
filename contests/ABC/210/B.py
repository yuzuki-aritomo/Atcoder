import io
import sys
_INPUT = """\
3
010
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

for i in range(N):
  if(S[i] == "1"):
    if(i%2 == 0):
      print("Takahashi")
    else:
      print("Aoki")
    exit()