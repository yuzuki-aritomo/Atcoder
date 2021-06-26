import io
import sys
_INPUT = """\
keyence

"""
sys.stdin = io.StringIO(_INPUT)

S = input()
if(S[0:7] == "keyence"):
  print("YES")
elif(S[-7:] == "keyence"):
  print("YES")
else:
  for i in range(7):
    w = S[0:7-i] + S[-i:]
    if(w == "keyence"):
      print("YES")
      exit()
  print("NO")