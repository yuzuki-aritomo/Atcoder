import io
import sys
_INPUT = """\
whbrjpjyhsrywlqjxdbrbaomnw
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())

Ans = float("inf")

for k in range(97, 123):
  w = chr(k)
  T = S.copy()
  # print(T, w)
  for j in range(len(S)):
    if(len(T) == T.count(w)):
      Ans = min(Ans, j)
      break
    for i in range(len(T)-1):
      if(T[i] == w or T[i+1]==w):
        T[i] = w
      else:
        T[i] = S[i]
    T.pop()

print(Ans)