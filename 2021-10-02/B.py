import io
import sys
_INPUT = """\
aabb
bbaa


"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()

if(S == T):
  print("Yes")
  exit()
elif(len(S) != len(T)):
  print("No")
  exit()

S = list(S)
for i in range(len(T)-1):
  tmp = S.copy()
  tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
  # print("".join(tmp), T)
  if("".join(tmp) == T):
    print("Yes")
    exit()

print("No")

