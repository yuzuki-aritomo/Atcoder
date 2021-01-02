import io
import sys

_INPUT = """\
5
2 1
2 1
2 1
2 1
2 1
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
C = []
A = 0
B = 0
for i in range(n):
    x,y = map(int, input().split())
    tmp = 2*x + y
    C.append([tmp,x,y])
    B += x
C.sort(reverse=True)

i = 0
ans = 0
tmp = 0
while(True):
    ans += 1
    A += (C[i][1] + C[i][2])
    tmp += C[i][1]
    i += 1
    if(A>(B-tmp)):
        print(ans)
        break
