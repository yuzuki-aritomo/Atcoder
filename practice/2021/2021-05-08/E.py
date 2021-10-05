import io
import sys
_INPUT = """\
2 5
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

i = 2
tmp = 0
Flag = 0
while(True):
    tmp += i*(i-1)//2
    if(tmp>K):
        Flag = i
        break
    i += 1

toAns =  tmp -((Flag-1)*(Flag-2)//2) - K
Anstmp = toAns

i = 0
j = Flag-1
tmp = 0
while(True):
    if(toAns - j > 0):
        toAns -= j
        tmp += 1
        j -= 1
    else:
        break

a = Anstmp +  tmp +1
b = j - toAns + 1
c = K - a - b
print("a:", a)
print("b:", b)
print("c:", c)



