import io
import sys
_INPUT = """\
4
1 1 2
2 1 4
3 0
4 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = [[0]]
for i in range(n):
    tmp = list(map(int,input().split()))
    A.append(tmp[1:])

print("A:", A)

color = [0 for i in range(n+1)]
S = [0 for i in range(n+1)]
F = [0 for i in range(n+1)]

time = 1

M = [1]
while(len(M)!=0):
    tmp = M[-1]
    color[tmp] = 1
    S[tmp] = time
    time += 1
    nxt = A[tmp][0]
    if(color[nxt]==0):
        M.append(nxt)
    else:
        M.pop()
        F[tmp] = time
        time += 1

for i in range(1,n+1):
    print(i, S[i],F[i])