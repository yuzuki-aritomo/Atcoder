import io
import sys
_INPUT = """\
1

"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
if n>=42:
  n += 1
a = str(n)
if len(a) ==1:
  a = "0"+a
print("AGC0"+a)
