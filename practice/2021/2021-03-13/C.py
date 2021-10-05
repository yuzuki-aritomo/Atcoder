import io
import sys
_INPUT = """\
27182818284590
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

N_str = str(N)
k = len(N_str)

# print("k:", k)

A = [999*10**(3*n) for n in range(6)]
A.insert(0, 0)

ans = 0
minus = ""
for i in range(((k-1)//3)*3):
    minus += "9"

# print("A:", A)

if(minus==""):
    m = 0
else:
    m = int(minus)

ans += (N - m)*((k-1)//3)
# print(ans)
# print("ans:", ans)

for i in range(((k-1)//3) + 1):
    if(i>=2):
        ans += A[i] * (i-1)
    else:
        ans += 0

# ans += A[((k-1)//3)]*(k-1)//3

print(ans)