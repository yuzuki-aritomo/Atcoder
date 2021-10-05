import io
import sys
_INPUT = """\
0BB1
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

Ans = []
for i in range(len(S)):
  if(S[i] == "0"):
    Ans.append("0")
  elif(S[i] == "1"):
    Ans.append("1")
  else:
    if(len(Ans) > 0):
      Ans.pop()

print("".join(Ans))