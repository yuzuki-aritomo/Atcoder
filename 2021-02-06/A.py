import io
import sys
_INPUT = """\
10 3 5 30
"""
sys.stdin = io.StringIO(_INPUT)

V, T, S, D = map(int, input().split())

if(V*T<=D and D<=V*S):
    print("No")
else:
    print("Yes")