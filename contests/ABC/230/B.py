import io
import sys
_INPUT = """\
ox
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
# oxx
tmp = "oxx"*4
tmp1 = "x"+ "oxx"*4
tmp2 = "xx" + "oxx"*4


if(tmp[:len(S)]==S):
  print("Yes")
elif(tmp1[:len(S)]==S):
  print("Yes")
elif(tmp2[:len(S)]==S):
  print("Yes")
else:
  print("No")
