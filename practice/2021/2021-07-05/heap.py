import io
import sys
_INPUT = """\
insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end
"""
sys.stdin = io.StringIO(_INPUT)


A = []
def insert(k):
  A.append(k)
  h = len(A)-1
  while(h>0):
    if(A[(h-1)//2] < A[h]):
      A[(h-1)//2], A[h] = A[h], A[(h-1)//2]
      h = (h-1)//2
    else:
      return
  return

def extract(k):
  ans = A[0]
  A[0] = A[-1]
  A.pop()
  h = 0
  while(h*2+1 < len(A)):
    n = h*2+1
    m = min(h*2+2, len(A)-1)
    if(A[h] < A[n] or A[h] < A[m]):
      if(A[n] < A[m]):
        A[h], A[m] = A[m], A[h]
        h = m
      else:
        A[h], A[n] = A[n], A[h]
        h = n
    else:
      return ans
  return ans

def main():
  while(True):
    S = input()
    if(S == "end"):
      return
    else:
      if(S == "extract"):
        print(extract(int(i)))
      else:
        s, i = S.split()
        insert(int(i))

main()