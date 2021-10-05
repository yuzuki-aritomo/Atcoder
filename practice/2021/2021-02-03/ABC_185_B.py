import io
import sys
_INPUT = """\
20 1 30
1 10
"""
sys.stdin = io.StringIO(_INPUT)

N, M, T = map(int, input().split())
N_max = N
time = 0
for i in range(M):
    a, b = map(int, input().split())
    N -= (a - time)
    time = b
    if(N<=0):
        print("No")
        exit()
    N += (b-a)
    if(N_max<N):
        N = N_max
if(N-T+time<=0):
    print("No")
else:
    print("Yes")
