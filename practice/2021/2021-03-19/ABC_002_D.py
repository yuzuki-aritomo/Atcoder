import io
import sys
_INPUT = """\
12 0
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = [[0 for i in range(N+1)] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    A[a][b] = 1
    A[b][a] = 1
    A[a][a] = 1
    A[b][b] = 1

def solve(people):
    for item in people:
        for peo in people:
            if(A[item][peo] != 1):
                return False
    return True

ans = 1
for i in range(2**N):
    people = []
    for k in range(N):
        if(i >>k &1):
            people.append(k+1)
    if(solve(people)):
        ans = max(ans, len(people))
print(ans)

