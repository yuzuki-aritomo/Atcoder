import io
import sys
_INPUT = """\
1
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
B = make_divisors(N*2)

ans = 0
for item in A:
    if(item%2==1):
        ans += 1
for item in B:
    if(item%2==1):
        ans += 1
print(ans)