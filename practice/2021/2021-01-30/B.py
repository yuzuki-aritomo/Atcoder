import io
import sys
_INPUT = """\
7 100 100
10 11
12 67
192 79
154 197
142 158
20 25
17 108
"""
sys.stdin = io.StringIO(_INPUT)

N, S, D = map(int, input().split())
for i in range(N):
    a,b = map(int, input().split())
    if(a<S and b>D):
        print("Yes")
        exit()
print("No")