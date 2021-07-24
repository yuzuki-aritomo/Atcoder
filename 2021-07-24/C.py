import io
import sys
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

mod = 10**9+7

S = input()

C = 0
H = 0
O = 0
K = 0
U = 0
D = 0
A = 0
I = 0

for i in range(len(S)):
  if(S[i] == "c"):
    C += 1
  elif(S[i] == "h"):
    H += C%mod
  elif(S[i] == "o"):
    O += H%mod
  elif(S[i] == "k"):
    K += O%mod
  elif(S[i] == "u"):
    U += K%mod
  elif(S[i] == "d"):
    D += U%mod
  elif(S[i] == "a"):
    A += D%mod
  elif(S[i] == "i"):
    I += A%mod

print(I%mod)