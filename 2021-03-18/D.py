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
maxlist = A[N-1]+1
Ans = [0 for i in range(maxlist)]

for item in A:
    Ans[item] += 1

for item in A:
    if(Ans[item]==0):
        continue
    i = 2
    while(item*i < maxlist):
        if(Ans[item]==0):
            break
        Ans[item*i] = 0
        i += 1
ans = 0
for item in Ans:
    if item==1 : ans+=1

print(ans)