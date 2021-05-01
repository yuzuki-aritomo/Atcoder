import io
import sys
_INPUT = """\
helloAtZoner
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
Ans = 0
for i in range(len(S)):
    if(S[i:i+4] == "ZONe"):
        Ans += 1

print(Ans)