import io
import sys
_INPUT = """\
3 3
1 7
3 2
1 7
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(list(map(int,input().split())))

def solve(i):
    S = str(i)
    for item in A:
        if(S[item[0]-1] != str(item[1])):
            return False
    return True

if(N==1):
    for i in range(10):
        if(solve(i)):
            print(i)
            exit()
elif(N == 2):
    for i in range(10, 100):
        if(solve(i)):
            print(i)
            exit()
else:
    for i in range(100, 1000):
        if(solve(i)):
            print(i)
            exit()

print(-1)