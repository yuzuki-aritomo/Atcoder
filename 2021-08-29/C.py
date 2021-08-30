n = int(input())
ans = ""
while(True):
    if(n == 1):
        ans = "A"+ans
        break
    elif(n%2 == 0):
        n //=2
        ans = "B" + ans
    else:
        n -= 1
        ans = "A"+ans
    
print(ans)