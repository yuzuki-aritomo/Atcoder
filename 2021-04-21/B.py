import io
import sys
_INPUT = """\
6
1 1
2 2
3 3
4 4
5 5
6 6
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = 0
for i in range(N):
    a, b = map(int,input().split())
    if(a == b):
        ans += 1
    else:
        ans = 0
    if(ans == 3):
        print("Yes")
        exit()
print("No")

