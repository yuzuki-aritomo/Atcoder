H = [4,3,3,4,5]

def isHeap():
  d = len(H)-1
  while(d > 0):
    if(H[d//2]>H[d]):
      return False
    d -= 1
  return True

print(isHeap())