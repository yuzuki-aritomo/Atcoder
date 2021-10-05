import io
import sys

_INPUT = """\
20 3
0 5 15
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    K, N = map(int,input().split())
    A = [int(x) for x in input().split()]
    l = 0
    for i in range(N-1, 0, -1):
        if(l < A[i] - A[i-1]):
            l = A[i] - A[i-1]
    if(l < K - A[-1] + A[0]):
        l = K - A[-1] + A[0]
    print(K - l)
main()