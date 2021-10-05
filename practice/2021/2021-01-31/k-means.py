import matplotlib.pyplot as plt

data = [
    [101, 11, 770000],
    [102, 9, 702000],
    [103, 7, 784000],
    [104, 10, 80000],
    [105, 5, 470000],
    [106, 2, 520000],
    [107, 1, 46000],
    [108, 7, 434000],
    [109, 3, 44700],
    [110, 1, 68000],
]

#クラスタ数
K = 3
#前処理を終えたデータを格納
dataX = []
#所属クラスターを保存
data_cluster = [0]*len(data)

#データの前処理
#x,yの値は近いほうがいいため100000で割る
#顧客番号はindex+101
for item in data:
    dataX.append([item[1],item[2]//100000])

#centersの初期値
centers = [
    [2,10],
    [8,1],
    [10,8],
]
distances = [0 for i in range(K)]
# ループ上限回数まで繰り返し
for loop in range(10000):
        # 入力データ全てに対して繰り返し
    for i in range(len(dataX)):
        # データから各重心までの距離を計算（ルートを取らなくても大小関係は変わらないので省略）
        for j in range(K):
            distances[j] = (centers[j][0]-dataX[i][0])**2+(centers[j][1]-dataX[i][1])**2
        # データの所属クラスタを距離の一番近い重心を持つものに更新
        data_cluster[i] = distances.index(min(distances))
    # すべてのクラスタに対して重心を再計算
    for i in range(K):
        x = 0
        y = 0
        n = 0
        for j in range(len(dataX)):
            if(data_cluster[j] == i):
                x += dataX[j][0]
                y += dataX[j][1]
                n += 1
        if(n==0):
            break
        centers[i][0] = x/n
        centers[i][1] = y/n

print("1191100011 有友柚樹")
print("各idとクラスター")
for i in range(len(data_cluster)):
    print("顧客番号：{0}, 渡航回数：{1}, 支払金額：{2}, クラスター：{3}".format(data[i][0],data[i][1],data[i][2],data_cluster[i]))


x, y = zip(*dataX)
for i in range(len(dataX)):
    if(data_cluster[i] == 0):
        plt.scatter(dataX[i][0], dataX[i][1],c="r",s=10,alpha=0.5)
    elif(data_cluster[i]==1):
        plt.scatter(dataX[i][0], dataX[i][1],c="b",s=10,alpha=0.5)
    else:
        plt.scatter(dataX[i][0], dataX[i][1],c="g",s=10,alpha=0.5)
plt.show()