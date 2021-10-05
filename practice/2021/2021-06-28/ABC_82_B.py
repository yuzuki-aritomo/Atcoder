import io
import sys
_INPUT = """\
zzz
zzz


"""
sys.stdin = io.StringIO(_INPUT)


S = list(input())
T = list(input())

S.sort()
T.sort(reverse=True)

# print(S)
# print(T)

if(S<T):
  print("Yes")
else:
  print("No")
# print(S<T)