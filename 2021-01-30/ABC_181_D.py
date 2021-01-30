import io
import sys
_INPUT = """\
256453
"""
sys.stdin = io.StringIO(_INPUT)

import collections

N = input()

if(len(N)<3):
    if(int(N%8) ==0 or int(N[::-1])):
        print("Yes")
    else:
        print("No")
    exit()

cnt  = collections.Counter(N)

for i in range(112, 1000,8):
    if not collections.Counter(str(i)) - cnt:
        print("Yes")

print("No")