import io
import sys

_INPUT = """\
3 1000000
1000 100
1000 100
1000 100
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int,input().split())
A =[]
for i in range(N):
    A.append(list(map(int,input().split())))

now = 0
X = X*100
F = True
for i in range(N):
    now += (A[i][0]*A[i][1])
    if(now > X):
        F = False
        print(i+1)
        break
if(F):
    print(-1)