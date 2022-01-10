import random
numer = []
#num = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(4):
    for j in range(4):
        #num[i][j] = random.randint(0, 1)
        numer.append(random.randint(0, 1))

#for _ in num:
#    print(_)
k = 0
for i in numer:
    if k % 4 == 0:
        print()
    print(i, end = ' ')    
    k += 1
