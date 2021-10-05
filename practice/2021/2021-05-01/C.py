import collections
import io
import sys
_INPUT = """\
ozRnonnoeR
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque
S = input()
Ans = deque()
tmp = 0
for i in range(len(S)):
    if(S[i] == "R"):
        tmp += 1
    elif(tmp%2 == 0):
        if(len(Ans)>0 and S[i] == Ans[-1]):
            Ans.pop()
        else:
            Ans.append(S[i])
    else:
        if(len(Ans)>0 and S[i] == Ans[0]):
            Ans.popleft()
        else:
            Ans.appendleft(S[i])

if(tmp%2 == 0):
    print("".join(Ans))
else:
    Ans = list(Ans)[::-1]
    print("".join(Ans))