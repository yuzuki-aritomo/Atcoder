import io
import sys
_INPUT = """\
6 3 3
7
6
2
8
10
6
"""
sys.stdin = io.StringIO(_INPUT)

N, C, K = map(int, input().split())
A = []
for i in range(N):
  A.append(int(input()))
A.sort(reverse=True)

# print(A)
# Ans = 0
# Wait = 0
# while(len(A) > 0):
#   if(Wait == C):
#     Ans += 1
#     Wait = 0
#     print(A)
#     continue
#   T = A.pop()
#   Wait += 1
#   if(len(A) > 0 and T + K >= A[-1]):
#     continue
#   else:
#     print(A)
#     Wait = 0
#     Ans += 1

Ans = 0
def solve(A, Wait, T):
  global Ans, K, C
  if(Wait == C):
    # print(A)
    Ans += 1
  elif(len(A)>0 and T+K >= A[-1]):
    A.pop()
    solve(A, Wait+1, T)
  else:
    # print(A)
    Ans += 1


while(len(A)>0):
  T = A.pop()
  solve(A, 1, T)

print(Ans)



