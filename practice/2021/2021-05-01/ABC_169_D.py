import io
import sys
_INPUT = """\
997764507000
"""
sys.stdin = io.StringIO(_INPUT)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
A = factorization(N)
Ans = 0

S = [1]
for i in range(2, 40):
    S.append(S[-1] + i)

Ans = 0
for item in A:
    if(item[0] == 1):
        break
    for i in range(len(S)):
        if(item[1]>=S[i]):
            tmp = i+1
    Ans += tmp
print(Ans)