import io
import sys
_INPUT = """\
abcabcabcabc
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
N = len(S)
if(N%2 == 1):
  S = S[0:len(S)-1]
else:
  S = S[0:len(S)-2]
i = 0
while(True):
  if(S[0: len(S)//2] == S[len(S)//2:]):
    print(len(S))
    exit()
  else:
    S = S[0:len(S) - 2]

