import io
import sys
_INPUT = """\
#.
.#
"""
sys.stdin = io.StringIO(_INPUT)

A = input()
B = input()

if A[1]=="." and B[0]==".":
  print("No")
elif A[0] == "." and B[1] ==".":
  print("No")
else:
  print("Yes")
