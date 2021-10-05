import io
import sys
_INPUT = """\
6 727202214173249351
6 5 2 5 3 2
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int,input().split()))

A.insert(0,0)
B = [0]*(N+1)
B[1] = 1
C = [1]
now = 1
for i in range(1, K+1):
    now = A[now]
    C.append(now)
    if(B[now] == 1):
        break
    B[now] = 1
    if(i==K):
        print(now)
        exit()

a =  C.index(now)
cycle = i - a
d = (K-i)%cycle
# print("C:", C)
# print("a:", a)
# print("cycle:", cycle)
# print("d:", d)
print(C[a+d])
