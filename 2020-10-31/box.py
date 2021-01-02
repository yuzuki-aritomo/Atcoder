import io
import sys

_INPUT = """\
1000000000 987654321 123456789
"""
sys.stdin = io.StringIO(_INPUT)

num = input().split()
# print(a[1])
a = int(num[0])
b = int(num[1])
c = int(num[2])

n = 0
sumA = 0
sumB = 0
sumC = 0


sumA = int((a)*(a+1)//2)
sumB = int((b)*(b+1)//2)
print((b)*(b+1))
print(sumB)
sumB = int((b)*(b+1)/2)
print((b)*(b+1))
print(sumB)

sumC = int((c)*(c+1)//2)

# print(sumB)

n = sumA*sumB*sumC

print(int(n%998244353))

# A, B, C = map(int, input().split())
# sum = A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2
# print(sum % 998244353)


