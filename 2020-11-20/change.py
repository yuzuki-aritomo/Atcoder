import io
import sys

_INPUT = """\
54321
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

ans = 0

ans += n//25
n = n%25

ans += n//10
n = n%10

ans += n//5
n = n%5

ans += n

print(ans)