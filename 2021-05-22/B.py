import io
import sys
_INPUT = """\
01010

"""
sys.stdin = io.StringIO(_INPUT)


S = list(input())

for i in range(len(S)):
    if(S[i]=="6"):
        S[i] = "9"
    elif(S[i] == "9"):
        S[i] = "6"

print("".join(S[::-1]))

