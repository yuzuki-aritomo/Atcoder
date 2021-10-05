import io
import sys
_INPUT = """\
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""
sys.stdin = io.StringIO(_INPUT)

A = list(map(int,input().split()))

ans = ["" for i in range(len(A))]

for i in range(len(A)):
  ans[i] = chr(A[i]+96)

print("".join(ans))