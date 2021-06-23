import io
import sys
_INPUT = """\
3
3200 3200 3200
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))
R = [0 for _ in range(9)]

for i in range(N):
  if(A[i]>= 3200):
    R[-1] += 1
    continue
  R[A[i]//400] += 1

Min = 0
Max = 0
for i in range(len(R)-1):
  if(R[i] != 0):
    Min += 1
Max = Min + R[-1]
if(Min == 0):
  Min = 1

print(Min, Max)