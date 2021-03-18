import io
import sys
_INPUT = """\
10
33 18 45 28 8 19 89 86 2 4
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A.sort()
Ans = [0 for i in range(1000005)]

for item in A:
    if(Ans[item]!=0):
        Ans[item] = 2
    else:
        Ans[item] = 1

for item in A:
    if(Ans[item]>=3):
        continue
    i = 2
    while(item*i < 1000005):
        Ans[item*i] += 2
        i += 1
ans = 0
for item in Ans:
    if item==1 : ans+=1

print(ans)