import io
import sys
_INPUT = """\
5 5
.....
.....
.###.
.###.
.....
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
A = []
for i in range(H):
    tmp = input()
    a = [0 for i in range(W)]
    for j in range(W):
        if(tmp[j]=="#"):
            a[j] = 1
    A.append(a)
ans = 0
s = 0
g = 0
for i in range(1, H-1):
    for j in range(1, W-1):
        if(A[i][j] == 1):
            tmp_s = s
            tmp_g = g
            s = j
            while(A[i][j]==1):
                g = j
                j += 1
            if(tmp_g !=g):
                ans += 2
            if(tmp_s != s):
                ans += 2
            break
if(ans == 1 and ans==2):
    print(4)
    exit()

print(ans)