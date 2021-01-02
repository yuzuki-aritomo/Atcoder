import io
import sys

_INPUT = """\
2525 -425
"""
sys.stdin = io.StringIO(_INPUT)


num = input().split()
n = int(num[0])
k = int(num[1])

ans = 0

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            for d in range(1,n+1):
                if(a + b - c- d == k):
                    ans += 1
print(ans)