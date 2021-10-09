import io
import sys
_INPUT = """\
2 22
6 37



"""
sys.stdin = io.StringIO(_INPUT)

N, P = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
  if(A[i]<P):
    ans += 1

print(ans)