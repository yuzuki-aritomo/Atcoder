import io
import sys
_INPUT = """\
100000000
"""
sys.stdin = io.StringIO(_INPUT)

tmp = 0
N = int(input())
for i in range(10**9):
  tmp += i
  if(N<=tmp):
    print(i)
    exit()
