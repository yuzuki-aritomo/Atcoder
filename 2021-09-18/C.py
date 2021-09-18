import io
import sys
_INPUT = """\
zyxwvutsrqponmlkjihgfedcba
5
a
ab
abc
ac
b
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*100000)

X = input()
N = int(input())
A = []
for i in range(N):
  A.append(input())

def diff(a, b):
  j = 0
  i = 0
  # for i in range(len(X)):
  while(True):
    if(len(a)==j or len(b) == j):
      if(len(a)<len(b)):
        return True
      else:
        return False
    elif(X[i] == a[j] and X[i] == b[j]):
      j += 1
      i = 0
      continue
    elif(X[i] == a[j]):
      return True
    elif(X[i] == b[j]):
      return False
    else:
      i += 1



def quick_sort(arr):
  left = []
  right = []
  if len(arr) <= 1:
    return arr
  # データの状態に左右されないためにrandom.choice()を用いることもある。
  # ref = random.choice(arr)
  ref = arr[0]
  ref_count = 0

  for ele in arr:
    if(ele ==ref):
      ref_count += 1
    elif diff(ele, ref):
      left.append(ele)
    else:
      right.append(ele)
  left = quick_sort(left)
  right = quick_sort(right)
  return left + [ref] * ref_count + right

for item in quick_sort(A):
  print(item)







