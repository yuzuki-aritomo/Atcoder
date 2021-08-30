n = int(input())
s = set()
for i in range(n):
    a,b = input().split()
    m = a+"_"+b

    if m in s:
        print("Yes")
        exit()
    else:
        s.add(m)
print("No")