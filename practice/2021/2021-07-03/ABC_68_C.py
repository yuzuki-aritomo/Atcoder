import io
import sys
_INPUT = """\
5 5
1 3
4 5
2 3
2 4
1 4
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

toP = []
toG = []
for i in range(M):
  a, b = map(int, input().split())
  if(a == 1):
    toP.append(b)
  elif(b == N):
    toG.append(a)

# print(toP)
# print(toG)

P = set(toP)
for item in toG:
  if item in P:
    print("POSSIBLE")
    exit()

print("IMPOSSIBLE")
