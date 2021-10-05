class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def PreOrder(T,a):
    if(a==None):
        return
    print(" {0}".format(a), end="")
    PreOrder(T, T[a].left)
    PreOrder(T, T[a].right)

def InOrder(T,a):
    if(a==None):
        return
    InOrder(T, T[a].left)
    print(" {0}".format(a), end="")
    InOrder(T, T[a].right)

def Insert(T, z, FirstNode):
    x = FirstNode
    while(x != None):
        y = x
        # print(x)
        if( z < T[x].key):
            x = T[x].left
        else:
            x = T[x].right
    T[z] = Node(z)
    T[z].parent = y
    if( z < T[y].key):
        T[y].left = z
    else:
        T[y].right = z

def Find(T, FirstNode, v):
    x = FirstNode
    while(x != None and x != v):
        if(x > v):
            x = T[x].left
        else:
            x = T[x].right
    if(x==v):
        return True
    else:
        return False

def Delete(T,z):
    global FirstNode
    if(T[z].left==None or T[z].right == None):
        v = z
    else:
        v = getSuccessor(T, T[z].right)
    v_p = T[v].parent
    if(T[v].left == None and T[v].right == None):
        v_chi = None
    elif(T[v].left == None):
        v_chi = T[v].right
    elif(T[v].right == None):
        v_chi = T[v].left
    
    if(v_p == None):
        FirstNode = v
        if(v_chi != None):
            T[v_chi].parent = None
    elif(T[v_p].left == v):
        T[v_p].left = v_chi
        if(v_chi != None):
            T[v_chi].parent = v_p
    else:
        T[v_p].right = v_chi
        if(v_chi != None):
            T[v_chi].parent = v_p
    
    if(v != z):
        T[z].key = v
        T[v] = T[z]
    T.pop(z)

def getSuccessor(T, a):
    while(T[a].left != None):
        v = T[a].left
    return a


def main():
    N = int(input())
    T = dict()
    Flag = 0
    FirstNode = -1
    for i in range(N):
        A = input()
        if("insert"==A[:6]):
            A, n = A.split()
            n = int(n)
            if(Flag==0):
                FirstNode = n
                T[n] = Node(n)
                Flag = 1
                continue
            Insert(T,n,FirstNode)
        elif("find" == A[:4]):
            A, n = A.split()
            n = int(n)
            if(Find(T, FirstNode, n)):
                print("yes")
            else:
                print("no")
        elif("delete" == A[:6]):
            A, n = A.split()
            n = int(n)
            Delete(T, n)
        else:
            InOrder(T, FirstNode)
            print()
            PreOrder(T, FirstNode)
            print()

main()
