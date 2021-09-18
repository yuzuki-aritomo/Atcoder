import io
import sys
_INPUT = """\
a
b
c
1
"""
sys.stdin = io.StringIO(_INPUT)


ans = ""
A = []
for i in range(3):
  A.append(input())
t = input()
for i in range(len(t)):
  ans += A[int(t[i])-1]
print(ans)