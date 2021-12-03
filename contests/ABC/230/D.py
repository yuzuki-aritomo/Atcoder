import io
import sys
_INPUT = """\
3 3
1 2
4 7
5 9
"""
sys.stdin = io.StringIO(_INPUT)


N, D = map(int,input().split())
A = []
for i in range(N):
  A.append(tuple(map(int,input().split())))

print(A)
