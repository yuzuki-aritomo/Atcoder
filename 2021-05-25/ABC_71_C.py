import io
import sys
_INPUT = """\
0070
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import product

S = input()
n = len(S)-1

def p(bits):
    for i in range(n):
        print(S[i], end="")
        if(bits[i] == 1):
            print("+", end="")
        elif(bits[i] == 2):
            print("-", end="")
    print(S[-1] + "=7")

for bits in product([1,2], repeat=n):
    tmp = []
    hugou = []
    j = 0
    for i in range(n):
        if(bits[i] == 1):
            tmp.append(int(S[j:i+1]))
            hugou.append(1)
            j = i+1
        elif(bits[i] == 2):
            tmp.append(int(S[j:i+1]))
            hugou.append(2)
            j = i+1
    tmp.append(int(S[j:len(S)]))
    check = tmp[0]
    for i in range(len(hugou)):
        if(hugou[i]==1):
            check += tmp[i+1]
        else:
            check -= tmp[i+1]
    if(check == 7):
        p(bits)
        exit()
