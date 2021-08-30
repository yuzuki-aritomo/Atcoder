n,m = map(int,input().split())
M=[]
for i in range(m):
    k = int(input())
    M.append(list(map(int, input().split())))

S = set()
S_id = [0 for i in range(2*(10**5)+100)]

def Check(c):
    if c in S:
        S.remove(c)
        return True
    else:
        S.add(c)
        return False

tmp = []
for i in range(m):
    tmp.append( (M[i].pop(), i) )
    while(len(tmp)>0):
        c = tmp.pop()
        if(Check(c[0])):
            if(len(M[S_id[c[0]]])>0):
                #削除したものの次の値を追加
                tmp.append( (M[S_id[c[0]]].pop(), S_id[c[0]]) )
            if(len(M[c[1]])>0):
                tmp.append((M[c[1]].pop(), c[1]))
        else:
            S_id[c[0]] = c[1]


for i in range(m):
    if(len(M[i])!=0):
        print("No")
        exit()
print("Yes")
    