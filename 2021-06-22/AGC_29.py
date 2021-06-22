import io
import sys
_INPUT = """\
BWBWBW
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())
A = []
for i in range(len(S)):
  if(S[i] == "W"):
    A.append(i)

B =0
for i in range(len(A)):
  B += i
Ans = sum(A) - B
# print("A:", A)
print(Ans)
