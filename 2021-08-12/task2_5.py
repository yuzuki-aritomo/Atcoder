

#nCr mod 100000007を求める関数
def solve(n, r):
  mod = 100000007 #modの宣言
  #nがmodよりも大きい時、必ず割り切れるので0となる
  if(mod<=n):
    return 0
  #n! mod 100000007 を求め、aに代入
  a = 1
  for i in range(n, 2, -1):
    a = (a*i) % mod
  #r! mod 100000007 を求め、bに代入
  b = 1
  for i in range(r, 2, -1):
    b = (b*i) % mod
  #bの逆元を求め、bに代入
  b = SurplusPower(b, mod-2, mod)
  #(n-r)! mod 100000007 を求め、cに代入
  c = 1
  for i in range(n-r, 2, -1):
    c = (c*i) % mod
  #cの逆元を求め、cに代入
  c = SurplusPower(c, mod-2, mod)
  #それぞれa,b,cを掛け、100000007で余りを取る
  return (a*b*c)%mod

#(aのk乗)mod p を求める関数
def SurplusPower(a, k, p):
  mod = 100000007
  if(k==0):
    return 1
  if(k%2 == 0):
    d = SurplusPower(a, k//2, p)
    return (d*d)%mod
  if(k%2 == 1):
    return (a*SurplusPower(a, k-1, p))%mod

print(solve(1000, 140))