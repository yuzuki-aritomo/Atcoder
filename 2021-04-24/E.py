import io
import sys
_INPUT = """\
3 1
2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

def C(a,b):
    if(b==0):
        return a
    up = 1
    down = 1
    for i in range(b):
        up *= a
        a -= 1
    for j in range(1 ,b+1):
        down *= j
    return up//down

S = [0, 1]
for k in range(2,20):
    S.append(S[k-1]*k)

Ans = 0
for i in range(M):
    a, b, c = list(map(int,input().split()))
    for i in range(c):
        tmp = C(b, i) * C(N-b, a-i)
        print(tmp)
        Ans += S[tmp]*S[N-tmp]
print(C(2, 0))
print(C(1, ))
print(Ans)