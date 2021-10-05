import io
import sys
_INPUT = """\
8
84 87 78 16 94 36 87 93
50 22 63 28 91 60 64 27
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

tmp = float("inf")
for i in range(N):
  if(T[i]<tmp):
    m = i
    tmp = T[i]
# print(m)

ans = [0 for i in range(N)]
ans[m] = T[m]
for i in range(m, m+N):
  ans[i%N] = min(T[i%N], ans[i%N-1]+S[i%N-1])

for i in range(N):
  print(ans[i])

