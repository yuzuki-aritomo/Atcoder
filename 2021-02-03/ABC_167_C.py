import io
import sys
_INPUT = """\
8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2
"""
sys.stdin = io.StringIO(_INPUT)

N, M, X = map(int, input().split()) 
A = []

for i in range(N):
    A.append(list(map(int,input().split())))

#bit全探索
Ans = float("inf")
for bit in range(1<<N):
    ans = 0
    B = [0]*M
    for j in range(N):
        if((bit>>j)&1):
            ans += A[j][0]
            for i in range(len(B)):
                B[i] += A[j][i+1]
    if(min(B)>=X):
        Ans = min(ans, Ans)

if(Ans==float("inf")):
    print(-1)
else:
    print(Ans)
