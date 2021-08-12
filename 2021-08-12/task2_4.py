
#判定する数
n = 100000007

def isPrime(n):
  #n==1の時、nは素数
  if n == 1:
    return True
  #2から順番にnまで割り、割り切れる数がある場合約数があるため素数ではない。
  #ただし割り切れる場合必ず対になる数が存在するため割り切れるかの判定は2からroot nまで行う
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  #2からroot nまで割り切れる整数がなかった場合、nは素数となるのでTrueを返す
  return True

print(isPrime(n))