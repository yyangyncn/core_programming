# 文件信息
f = open(input('please input a file name: '), 'r')
num = 0

for i in f:
    num += 1

# num2 = len(f.readlines())

print('this file has ', num, ' lines')