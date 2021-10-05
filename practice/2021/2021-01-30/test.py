

for bit in range(1<<3):
    # print(bit)
    for i in range(3):
        a = 0
        if((bit>>i)&1):
            # print("i:", i)
            a += 1
            print("bit:", bit)
        print("a:", a)