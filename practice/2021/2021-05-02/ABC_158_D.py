import io
import sys
_INPUT = """\
y
1
2 1 x
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

S = input()
Q = int(input())

Ans = deque(S)
tmp = 0
for i in range(Q):
    Com = input()
    if(Com[0] == "1"):
        tmp += 1
    else:
        if(tmp%2==0):
            if(Com[2] == "1"):
                Ans.appendleft(Com[4])
            else:
                Ans.append(Com[4])
        else:
            if(Com[2] == "2"):
                Ans.appendleft(Com[4])
            else:
                Ans.append(Com[4])

if(tmp%2 == 0):
    print("".join(Ans))
else:
    Ans = list(Ans)[::-1]
    print("".join(Ans))