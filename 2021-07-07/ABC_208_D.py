import io
import sys
_INPUT = """\
5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2
5 2 5
5 3 6
5 4 5
"""
sys.stdin = io.StringIO(_INPUT)

INF = float("inf")
# INF = 1<<60

N, M = map(int, input().split())
A = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
  p0, p1, c = map(int, input().split())
  A[p0][p1] = min(c, A[p0][p1])

for i in range(N+1):
  A[i][i] = 0

Ans = 0
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      A[i][j] = min(A[i][k]+A[k][j], A[i][j])
      if(A[i][j] != INF):
        Ans += A[i][j]

print(Ans)