import io
import sys
_INPUT = """\
123456789 11119876543210
"""
sys.stdin = io.StringIO(_INPUT)

a, b = input().split()

for i in range(min(len(a), len(b))):
  if int(a[-i-1])+int(b[-i-1])>9:
    print("Hard")
    exit()
    
print("Easy")