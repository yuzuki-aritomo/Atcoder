import io
import sys
_INPUT = """\
2
na
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
s = input()

ans = ''
i = 0
while(True):
  if i >= n-1:
    if i == n-1:
      ans += s[i]
    break
  if s[i] == 'n' and s[i+1] == 'a':
    ans += 'nya'
    i += 2
  else:
    ans += s[i]
    i += 1

print(ans)
