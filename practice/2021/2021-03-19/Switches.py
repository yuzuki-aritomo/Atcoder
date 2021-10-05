import io
import sys
_INPUT = """\
2 2
2 1 2
1 2
0 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(M):
    tmp = list(map(int, input().split()))
    A.append(tmp[1:])
Lam = list(map(int,input().split()))

def solve(switch):
    # print(switch)
    for i in range(M):
        tmp = 0
        for item in A[i]:
            if(switch[item-1]):
                tmp += 1
        if(tmp%2 != Lam[i]):
            return False
    return True

ans = 0
for i in range(2**N):
    switch = [0 for i in range(N)]
    for j in range(N):
        if(i >> j & 1):
            switch[j] = 1
    if(solve(switch)):
        ans += 1
print(ans)
# print("A:", A)
# print("Lam:", Lam)