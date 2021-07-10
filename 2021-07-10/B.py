import io
import sys
_INPUT = """\
4 4
1 2 1 2
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int,input().split()))

ans = sum(A) - N//2

if(X>=ans):
  print("Yes")
else:
  print("No")
