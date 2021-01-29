import io
import sys
_INPUT = """\
720
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


A = make_divisors(int(input()))
for item in A:
    print(item)