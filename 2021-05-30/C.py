import io
import sys
_INPUT = """\
3 2
5 5
2 1
2 2
"""
sys.stdin = io.StringIO(_INPUT)


N, K = map(int, input().split())

F = []
for i in range(N):
    a, b = map(int, input().split())
    if(i !=0 and F[-1][0] == a):
        F[-1][1] += b
    else:
        F.append([a, b])
F.sort()

Ans = K
M = K
for i in range(len(F)):
    a, b = F[i][0], F[i][1]
    if(Ans<a):
        print(Ans)
        exit()
    else:
        Ans += b

print(Ans)