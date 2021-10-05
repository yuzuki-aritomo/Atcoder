import io
import sys
_INPUT = """\
insert 8
insert 7
insert 2
extract
insert 19
insert 10
extract
extract
insert 8
extract
extract
insert 3
insert 4
insert 1
extract
extract
extract
end
"""
sys.stdin = io.StringIO(_INPUT)


import heapq

A = []
def main():
  heapq.heapify(A)
  while(True):
    S = input()
    if(S == "end"):
      return
    else:
      if(S == "extract"):
        print(-heapq.heappop(A))
      else:
        s, t = S.split()
        heapq.heappush(A, -int(t))
main()