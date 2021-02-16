import io
import sys
_INPUT = """\
5 9
0 0
"""
sys.stdin = io.StringIO(_INPUT)

def solve(n, x):
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if(i+j+k == x):
                    ans += 1
    return ans

while(True):
    n, x = map(int, input().split())
    if(n==0 and x==0):
        break
    print(solve(n, x))
