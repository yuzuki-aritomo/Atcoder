def yakusu(n):
    A, B = [],[]
    i = 1
    while(i**2 <= n):
        if(n%i==0):
            A.append(i)
            if(n//i != i):
                B.append(n//i)
        i += 1
    return A + B[::-1]

print(yakusu(105))