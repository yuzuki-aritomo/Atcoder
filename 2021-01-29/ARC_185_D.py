import io
import sys
_INPUT = """\
5 5
5 2 1 4 3
"""
sys.stdin = io.StringIO(_INPUT)

def solve():
    A.sort()
    B = []
    # if(A[0]!=1):
    #     B.append(A[0]-1)
    # if(A[-1]!=N):
    #     B.append(N-A[-1])

    if(N-A[-1]!=0):
        B.append(N-A[-1])
    if(A[0]-1!=0):
        B.append(A[0]-1)

    for i in range(M-1):
        tmp = A[i+1]-A[i]-1
        if(tmp!=0):
            B.append(tmp)
    if(len(B)==0):
        minA=0
    else:
        minA = min(B)
    ans = 0
    if(minA==0):
        print(0)
    else:
        for item in B:
            if(item%minA==0):
                ans += item//minA
            else:
                ans += item//minA + 1
        print(ans)
# print("A:", A)
# print("B:", B)
# print("minA:", minA)

N, M = map(int, input().split())
if(M!=0):
    A = list(map(int,input().split()))
    solve()
else:
    print(1)