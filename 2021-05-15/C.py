import io
import sys
_INPUT = """\
xxxxx?xxxo
"""
sys.stdin = io.StringIO(_INPUT)
A = input()
a = []
b = []
c = []

for i in range(10):
    if(A[i]=="o"):
        a.append(i)
    elif(A[i] == "?"):
        b.append(i)
    else:
        c.append(i)

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                Flag = True
                for item in a:
                    if(item ==i or item==j or item==k or item==l):
                        continue
                    else:
                        Flag = False
                        break
                for item in c:
                    if(item!=i and item!=j and item!=k and item!=l):
                        continue
                    else:
                        Flag = False
                        break
                if(Flag):
                    ans += 1

print(ans)
