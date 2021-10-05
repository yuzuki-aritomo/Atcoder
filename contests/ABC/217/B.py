import io
import sys
_INPUT = """\
AGC
ABC
ARC

"""
sys.stdin = io.StringIO(_INPUT)

S = set()
S.add("ABC")
S.add("ARC")
S.add("AGC")
S.add("AHC")

for i in range(3):
  A = input()
  S.remove(A)

print(S.pop())
