import io
import sys
_INPUT = """\
1
1


"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

ans = [0 for _ in range(N)]

for i in range(N):
  ans[A[i]-1] = i+1

print(" ".join(map(str, ans)))