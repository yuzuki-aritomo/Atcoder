import io
import sys
_INPUT = """\
8691 20
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

for _ in range(K):
    if(N%200 == 0):
        N //= 200
    else:
        N = int( str(N) + "200" )

print(N)