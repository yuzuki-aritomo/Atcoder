import io
import sys
_INPUT = """\
101
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
i = 1
tmp = 7%K
S = set()
while(tmp != 0):
    if(tmp in S):
        print(-1)
        exit()
    else:
        S.add(tmp)
        tmp = (tmp * 10 + 7)%K
        i += 1

print(i)