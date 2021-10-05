import io
import sys
_INPUT = """\
869121
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

if(N<2):
    print(0)
    exit()
elif(N==2):
    print(2)
    exit()

ans = (10**N) % 1000000007
ans = ans - (2*(9**N)% 1000000007)
ans = ans + (8**N)% 1000000007
ans = ans % 1000000007
print(ans)
