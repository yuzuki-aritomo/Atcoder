import io
import sys

_INPUT = """\
3
4
3
2
"""
sys.stdin = io.StringIO(_INPUT)

def solve():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    ans = A[1] - A[0]
    mi = A[0]
    tmp = 0
    for item in A:
        if(tmp==0):
            tmp = 1
            continue
        a = item
        # print("a: ",a)
        if(mi > a):
            mi = a
            # print("mi: ",mi)
        else:
            b = a - mi
            # print("b:",b)
            if(ans < b ):
                ans = b
                # print("ans:",ans)
    print(ans)
solve()