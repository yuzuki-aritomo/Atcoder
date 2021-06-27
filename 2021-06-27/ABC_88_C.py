import io
import sys
_INPUT = """\
1 8 6
2 9 7
0 7 7


"""
sys.stdin = io.StringIO(_INPUT)

M = []
for i in range(3):
  M.append(list(map(int,input().split())))

def C(a, b, c):
  if(a == b and b == c):
    return False
  return True

for i in range(2):
  if(C(M[i+1][0] - M[i][0], M[i+1][1] - M[i][1], M[i+1][2] - M[i][2])):
    print("No")
    exit()
  if(C(M[0][i+1] - M[0][i], M[1][i+1] - M[1][i], M[2][i+1] - M[2][i])):
    print("No")
    exit()
print("Yes")


