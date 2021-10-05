
#ABC_182_B
N = int(input())
A = list(map(int, input().split()))
Ans = 0

for i in range(2, 1001):
	ans = 0
	for j in range(N):	
		if(A[j] % i == 0):
			ans += 1
	Ans = max(ans, Ans)
print(Ans)

#ABC_182_A
A, B = map(int, input().split())
print((2*A+100) - B)

#ABC_183_A
x = int(input())
print(max(x, 0))

#ABC_184_A
N, X = map(int, input().split())
S = input()

for i in range(N):
	if(S[i] == "o"):
		X += 1
	else:
		X -= 1
		X = max(X, 0)

print(X)

#ABC_183_A
a, b = map(int,input().split())
c, d = map(int,input().split())
print(a*d - c*b)