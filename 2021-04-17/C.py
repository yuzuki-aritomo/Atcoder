import io
import sys
_INPUT = """\
2 4
"""
sys.stdin = io.StringIO(_INPUT)

import math
from collections import Counter

A, B = map(int, input().split())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

Cnt = Counter()
for i in range(A, B+1):
    Cnt.update(make_divisors(i))

Ans = 1
for item in Cnt:
    if(Cnt[item] != 1):
        Ans = max(item, Ans)
print(Ans)
