import io
import sys
_INPUT = """\
5
1 5 7 10 21
4
2 4 17 8
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

def solve(ans):
    for bit in range(2**n):
        tmp = 0
        for i in range(n):
            if((bit>>i)&1):
                tmp += A[i]
        if(ans == tmp):
            return True
    return False

for item in M:
    if(solve(item)):
        print("yes")
    else:
        print("no")