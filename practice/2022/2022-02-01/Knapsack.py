
import random

class biont(): # 個体情報
  gene = [] # 遺伝情報
  value = 0 #価値
  weight = 0 # 重さ
  def __init__(self, gene):
    self.gene = gene
    self.check_max_weight()
    self.value = self.get_value()
    self.weight = self.get_weight()
  
  # 最大許容重量を計算、違反している場合単位あたりの価値の小さなものを削除
  def check_max_weight(self): 
    while(True):
      w = self.get_weight()
      if w > MaxWeight: # 違反しているとき
        min_v_per_w = min(Knapsack[i]['v_per_w'] for i, x in enumerate(self.gene) if x == 1)
        for index in [i for i, x in enumerate(self.gene) if x == 1]:
          if Knapsack[index]['v_per_w']==min_v_per_w:
            self.gene[index] = 0
      else:
        return
  
  def get_value(self): #価値を計算
    return sum(
      Knapsack[i]['v'] for i, x in enumerate(self.gene) if x == 1
    )

  def get_weight(self): #重量を計算
    return sum(
      Knapsack[i]['w'] for i, x in enumerate(self.gene) if x == 1
    )

#初期のランダムな遺伝子
def rand_gene():
  rand_0_1 = lambda: 0 if random.random() >= 0.5 else 1
  return [rand_0_1() for i in range(10)]

#一点交叉
def crossover(p0, p1):
  r = random.randint(1, 9)
  gene0 = p0.gene[0:r] + p1.gene[r:10]
  gene1 = p1.gene[0:r] + p0.gene[r:10]
  rand_0_1 = lambda: 0 if random.random() >= 0.9 else 1
  for i in range(len(gene0)): # 突然変異
    if rand_0_1==1: gene0[i] ^= 1
    if rand_0_1==1: gene1[i] ^= 1
  return biont(gene0), biont(gene1)

#初期値
MaxWeight = 35
Knapsack = [
  { 'v': 6, 'w': 3 , 'v_per_w': 2},
  { 'v': 0, 'w': 7 , 'v_per_w': 0},
  { 'v': 9, 'w': 2 , 'v_per_w': 4.5},
  { 'v': 8, 'w': 1 , 'v_per_w': 8},
  { 'v': 0, 'w': 6 , 'v_per_w': 0},
  { 'v': 4, 'w': 8 , 'v_per_w': 0.5},
  { 'v': 6, 'w': 4 , 'v_per_w': 1.5},
  { 'v': 3, 'w': 3 , 'v_per_w': 1},
  { 'v': 4, 'w': 8 , 'v_per_w': 0.5},
  { 'v': 9, 'w': 4 , 'v_per_w': 2.25},
]

# 初期化(第1世代)
Population = [ biont(rand_gene()) for _ in range(6) ]
Population.sort(key=lambda x: x.value, reverse=True)#適応度が高い順にソート
print('1世代目') #世代
print('平均適応度',sum(p.value for p in Population) / len(Population))# 平均適応度を出力
print('最大適応度', max(p.value for p in Population)) # 最大適応度を出力

for i in range(9):#世代ごと
  child0, child1 = crossover(Population[0], Population[1]) #交配
  child2, child3 = crossover(Population[2], Population[3])
  Population.extend([child0, child1, child2, child3])
  Population.sort(key=lambda x: x.value, reverse=True)#適応度が高い順にソート
  Population = Population[:6] # 世代更新
  print('-----------------------')
  print(i+2, '世代目') #世代
  print('平均適応度',sum(p.value for p in Population) / len(Population))# 平均適応度を出力
  print('最大適応度', max(p.value for p in Population)) # 最大適応度を出力
