a,b = input().split(".")
b = int(b)
ans = ""
if(b<=2):
  ans = a + "-"
  print(ans)
elif(b<=6):
  print(a) 
else:
  ans = a+"+"
  print(ans)