import io
import sys

_INPUT = """\
3
1 3 5
3 -6 3
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += A[i]*B[i]

if(ans==0):
    print("Yes")
else:
    print("No")