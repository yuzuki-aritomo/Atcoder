import io
import sys
_INPUT = """\
39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
Rn =  0
Gn =  0
Bn =  0
for i in range(N):
    if(S[i] == "G"): Gn+=1
    if(S[i] == "B"): Bn+=1
    if(S[i] == "R"): Rn+=1

ans = 0

for i in range(len(S)):
    k = 1
    while(True):
        if(i<0 or i+k*2 >= len(S)):
            break
        if(S[i+k]!=S[i] and S[i]!= S[i+k*2] and S[i+k*2]!=S[i+k]):
            ans += 1
        k+=1

print(Rn*Gn*Bn - ans)