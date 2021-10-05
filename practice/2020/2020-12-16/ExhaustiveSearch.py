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
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


S = []
def makeconbo():
    for i in range(n):
        S.append(0)
    rec(0)

def rec(i):
    if(i == n):
        print(S)
        return
    rec(i+1)    
    S[i] = 1
    rec(i+1)
    S[i] = 0

def solve(i,m):
    if(m==0):
        return True
    if(i>=n):
        return False
    res = solve(i+1,m) or solve(i+1,m-A[i])
    return res

def main():
    for item in B:
        if(solve(0,item)):
            print("yes")
        else:
            print("no")
main()