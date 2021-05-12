import io
import sys
_INPUT = """\
35897 932

"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
if(K%2==1):
    Ans = (N//K) ** 3
else:
    a = (N//(K)) **3
    if(N%K >= K//2):
        b = ((N//(K))+1) **3
    else:
        b = (N//(K)) **3
    Ans = a + b

print(Ans)