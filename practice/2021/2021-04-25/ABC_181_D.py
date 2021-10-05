import io
import sys
_INPUT = """\
1333
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter
Cnt = Counter()
S = input()

if(len(S)==2):
    if(int(S)%8 == 0):
        print("Yes")
        exit()
    else:
        S = S[1] + S[0]
        if(int(S)%8 == 0):
            print("Yes")
            exit()
        print("No")
    exit()
elif(len(S)==1):
    if(int(S)%8 == 0):
        print("Yes")
    else:
        print("No")
    exit()

S = Counter(S)

i = 14
while(i*8<=1000):
    n = str(i*8)
    if(n[0] == "0" or n[1] == "0" or n[2]=="0"):
        i += 1
        continue
    Cnt = Counter(n)
    F = True
    for item in Cnt:
        if(S[item] < Cnt[item]):
            F = False
    if(F):
        print("Yes")
        exit()
    i += 1
print("No")