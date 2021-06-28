import io
import sys
_INPUT = """\
1
a
z
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
T = input()
m = len(S) + len(T)

Ans = m
for i in range(m-N+1):
  if(S[-i:] == T[0:i]):
    Ans = m - i

print(Ans)

# same_num = 0
# for i in range(min(len(S), len(T))):
#   if(S[-(i+1)] == T[i]):
#     same_num += 1
#   else:
#     break

# print(max(N, m - same_num))
