import io
import sys
_INPUT = """\
3 4 2
1 7 7 9
9 6 3 7
7 8 6 4
"""
sys.stdin = io.StringIO(_INPUT)

H, W, C = map(int, input().split())
M = []
for i in range(H):
  M.append(list(map(int,input().split())))


