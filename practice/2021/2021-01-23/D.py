import io
import sys

_INPUT = """\
2
AND
OR
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
    A.append(input())
A.reverse()

print(A)

ans = 0
def search(n,i):
    global ans
    print(i)
    if(i==N):
        ans += 1
        print("ans",ans)
        return
    if(n==1 and A[i]=="AND"):
        print("--")
        search(1,i+1)
    elif(n==1 and A[i]=="OR"):
        print("---")
        search(1,i+1)
        search(0,i+1)
    elif(n==0 and A[i]=="AND"):
        return
    elif(n==0 and A[i]=="OR"):
        print("----")
        search(1,i+1)

search(1,0)
search(0,0)