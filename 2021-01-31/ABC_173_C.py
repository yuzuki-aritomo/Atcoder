import io
import sys
_INPUT = """\
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#
"""
sys.stdin = io.StringIO(_INPUT)

H, W, K = map(int, input().split())
A = [[0 for i in range(W)] for j in range(H)]

for i in range(H):
    com = input()
    for j in range(W):
        if(com[j]=="#"):
            A[i][j] = 1
        else:
            A[i][j] = 0

ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        tmp = 0
        for i_bit in range(H):
            for j_bit in range(W):
                if((i>>i_bit)&1):
                    if((j>>j_bit)&1):
                        if(A[i_bit][j_bit] == 1):
                            tmp += 1
        if(tmp==K):
            ans += 1

print(ans)