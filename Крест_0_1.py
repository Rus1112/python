#  1
# 010
#00100

n = int(input())

for i in range(n+1):
    print(' ' * (n-i+1) + '0'*i + '1' + '0'*i)
print('1'*(2*n+3))

for i in range(n, -1, -1):
    print(' ' * (n-i+1) + '0'*i + '1' + '0'*i)
