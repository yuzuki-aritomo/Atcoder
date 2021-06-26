import io
import sys
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())

M = []
for i in range(H):
  S = list(input())
  for j in range(W):
    if(S[j] != "."):
      M.append(S)
      break

tmp = []
for j in range(W):
  F = True
  for i in range(len(M)):
    if(M[i][j] != "."):
      F = False
      break
  if(F):
    tmp.append(j)

def change(item):
  w = ""
  for i in range(len(item)):
    if i in tmp:
      continue
    else:
      w += item[i]
  return w

for i in range(len(M)):
  word = change(M[i])
  print(word)