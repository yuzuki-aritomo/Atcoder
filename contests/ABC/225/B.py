import io
import sys
_INPUT = """\
10
9 10
3 10
4 10
8 10
1 10
2 10
7 10
6 10
5 9
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = [0 for i in range(N)]

for i in range(N-1):
  a, b = map(int, input().split())
  A[a-1] += 1
  A[b-1] += 1

for i in range(N):
  if(A[i]==N-1):
    print("Yes")
    exit()
print("No")
