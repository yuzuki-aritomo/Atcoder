import io
import sys
_INPUT = """\
2 3 2
..#
###
"""
sys.stdin = io.StringIO(_INPUT)

H, W, K = map(int, input().split())
A =[[0 for i in range(W)] for i in range(H)]
print(A)

for i in range(H):
    com = input()
    for k in range(W):
        if(com[k]=="#"):
            A[i][k] = 1

print("A:", A)

for i in range(2**H):
    for k in range(2**W):
        print("i:", i)
        print("k:", k)
