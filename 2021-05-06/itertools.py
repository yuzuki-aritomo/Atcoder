import itertools

ans = 0
def calc(i):
    global ans
    ans += i

for i in itertools.repeat(10, 3):
    print(i)

L = [0, 1, 2, 3, 4]
tmp = 0
for item in itertools.permutations(L, 5):
    tmp += 1
    # print("item:", item)
    # print(type(item))


A = (2, 3, "t")
print(A)

print("tmp:", tmp)

bit = list(itertools.product([0, 1], repeat=3))
print(bit)