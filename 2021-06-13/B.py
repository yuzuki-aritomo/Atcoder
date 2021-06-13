import io
import sys
_INPUT = """\
3
1 2 3


"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

A.sort()

for i in range(N):
  if(A[i] != i+1):
    print("No")
    exit()

print("Yes")