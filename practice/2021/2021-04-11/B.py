import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

N = input()
d = deque(N)

# print(d)
while(True):
    if(d[-1] != "0"):
        break
    d.pop()
    if(len(d)==0):
        print("Yes")
        exit()
# print(d)
while(True):
    if(len(d) == 0 or len(d) ==1):
        break
    if(d.pop() != d.popleft()):
        print("No")
        exit()
print("Yes")
