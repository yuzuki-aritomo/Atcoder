import io
import sys
_INPUT = """\
8 1000000000 1000000000
bcdfcgaa
"""
sys.stdin = io.StringIO(_INPUT)



n, a, b = map(int, input().split())
s = input()

m = []
for i in range(n//2):
  tmp = 0
  tmps = s[i:]+ s[:i]
  for j in range(n//2):
    if tmps[j] != tmps[-j-1]:
      tmp += 1
  m.append(tmp)


ans = float('inf')

for i in range(len(m)):
  ans = min(a*i + m[i]*b, ans)

print(ans)
