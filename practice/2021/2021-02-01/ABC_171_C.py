import io
import sys
_INPUT = """\
123456789
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
#文字数
i = 1
tmp = 26
while(N>tmp):
    i += 1
    tmp = tmp + 26**i
# print("i:", i)

A = []
for k in range(i):
    N -= 1
    A.append(N % 26)
    N = N//26

# print("A:", A)
ans = ""
for item in A:
    ans += chr(item+97)
print(ans[::-1])