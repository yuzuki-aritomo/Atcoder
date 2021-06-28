import io
import sys
_INPUT = """\
1 7 10
"""
sys.stdin = io.StringIO(_INPUT)

N, A, B = map(int, input().split())

# if(A>B):
#   print(0)
# else:
print(max(0,(B*(N-1)+A) - (A*(N-1)+B)+1))