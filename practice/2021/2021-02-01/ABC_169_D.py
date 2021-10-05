import io
import sys
_INPUT = """\
997764507000
"""
sys.stdin = io.StringIO(_INPUT)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N = int(input())
A = make_divisors(N)
A.pop(0)
ans = 0
for i in range(len(A)):
    z = A[i]
    if(z>N):
        break
    ans += 1
    N /= z
    if(N==1):
        break

print(ans)