import io
import sys
_INPUT = """\
7
123 456

"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
a, b = map(str, input().split())

A = 0
for i in range(len(a)):
  A += int(a[-(i+1)])*(K**i)
B = 0
for i in range(len(b)):
  B += int(b[-(i+1)])*(K**i)

print(A*B)


