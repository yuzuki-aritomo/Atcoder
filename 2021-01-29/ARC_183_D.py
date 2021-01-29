import io
import sys
_INPUT = """\
6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())

A = []
for i in range(N):
    a,b,c = map(int, input().split())
    A.append([a,c])
    A.append([b,-c])
A.sort()

now = 0
Falg = False
for item in A:
    now += item[1] 
    if(now>W):
        Falg = True
        break

if(Falg):
    print("No")
else:
    print("Yes")
