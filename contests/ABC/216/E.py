N, K = map(int,input().split())
A = list(map(int,input().split()))
A.append(0)
A.sort()

def SumU(m, n, k):
    return ((m+(m-n+1))*n//2)*k

#print(SumU(5, 3))

ans = 0
same = 1
for i in range(N,0,-1):
    m = A[i] - A[i-1]
    if(m*same<=K):
        ans += SumU(A[i], m, same)
        K -= m*same
        same += 1
    else:
        ans += SumU(A[i], K//same, same)
        ans += (A[i]-K//same)*(K%same)
        break
print(ans)