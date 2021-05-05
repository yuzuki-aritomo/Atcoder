import io
import sys
_INPUT = """\
30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
Ans = 0
for i in range(K):
    if(T[i] == "r"):
        Ans += P
    elif(T[i] == "s"):
        Ans += R
    elif(T[i] == "p"):
        Ans += S

for i in range(K, N):
    if(T[i] == "r"):
        if(T[i-K] == "r"):
            T[i] = "a"
            continue
        Ans += P
    elif(T[i] == "s"):
        if(T[i-K] == "s"):
            T[i] = "a"
            continue
        Ans += R
    elif(T[i] == "p"):
        if(T[i-K] == "p"):
            T[i] = "a"
            continue
        Ans += S

print(Ans)