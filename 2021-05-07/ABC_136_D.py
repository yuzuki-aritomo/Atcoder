import io
import sys
_INPUT = """\
RRRLLRLLRRRLLLLL
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
N = len(S)

R_Lind = [0 for _ in range(N)]
L_Rind = [0 for _ in range(N)]
Ans = [0 for _ in range(N)]

for i in range(N-1, -1, -1):
    if(S[i] == "L"):
        Lind = i
    R_Lind[i] = Lind
for i in range(N):
    if(S[i] == "R"):
        Rind = i
    L_Rind[i] = Rind

for i in range(N):
    Lind = R_Lind[i]
    Rind = L_Rind[i]
    if(S[i] == "R"):
        if((Lind - i )%2 == 0):
            Ans[Lind] += 1
        else:
            Ans[Lind-1] += 1
    elif(S[i] == "L"):
        if((i - Rind)%2 == 0):
            Ans[Rind] += 1
        else:
            Ans[Rind+1] += 1

print(" ".join(map(str, Ans)))