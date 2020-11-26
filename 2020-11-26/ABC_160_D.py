import io
import sys

_INPUT = """\
5 2 4
"""

def main():
    N, X, Y = map(int,input().split())
    L = {}
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            tmp = min(j - i,abs(i-X)+1+abs(j-Y))
            if tmp in L:
                L[tmp] += 1
            else:
                L[tmp] = 1
    for i in range(1,N):
        if i not in L:
            print(0)
        else:
            print(L[i])
main()