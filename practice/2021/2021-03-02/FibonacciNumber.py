import io
import sys
_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

N = int(input())
Memo = [0] * (N+1)
def fibo(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    if(Memo[n]!=0):
        return Memo[n]
    Memo[n] = fibo(n-1) + fibo(n-2)
    return Memo[n]
print(fibo(N))