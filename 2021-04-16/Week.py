import io
import sys
_INPUT = """\
11
1 1 1 0 1 1 1 0 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
D = list(map(int,input().split()))
Cnt = Counter(D[0:7])
Ans = 0
if(Cnt[0]< 2):
    ans = 0
else:
    ans = 7
for i in range(N-7):
    Cnt[D[i]] -= 1
    Cnt[D[i + 7]] += 1
    if(Cnt[0] < 2):
        Ans = max(Ans, ans)
        ans = 0
    else:
        ans += 1
        if(ans < 7):
            ans = 7
Ans = max(Ans, ans)
print(Ans)



