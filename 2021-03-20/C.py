import io
import sys
_INPUT = """\
333
"""
sys.stdin = io.StringIO(_INPUT)

N = input()
leng = len(N)

A = [
    0,
    9,
    99, 
    999,
    9999, 
    99999, 
    999999, 
    9999999, 
    99999999,
    999999999,
    9999999999,
    99999999999,
    999999999999,
]
if(leng%2 == 1):
    print(A[leng//2])
else:
    ans = A[leng//2-1]
    pre = N[:leng//2]
    nxt = N[leng//2:]
    if(int(pre) <= int(nxt)):
        ans += int(pre)-A[leng//2-1]
    else:
        ans += int(pre)-A[leng//2-1]-1
    print(ans)


