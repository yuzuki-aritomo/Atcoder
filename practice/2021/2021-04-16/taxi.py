import io
import sys
_INPUT = """\
3 600
600 200 200 400
900 800 400 500
200 200 200 300
"""
sys.stdin = io.StringIO(_INPUT)

N, L = map(int, input().split())
Fee = []
for i in range(N):
    Fee.append(list(map(int,input().split())))

Ans = []
for F in Fee:
    if(L< F[0]):
        Ans.append(F[1])
    else:
        ans = F[1]
        nex = L - F[0]
        ans +=  (nex//F[2] + 1) * F[3]
        Ans.append(ans)
print(min(Ans), max(Ans))

