# 文件访问
import os
f = open(input('please input a file name: '), 'r', encoding='GBK')

num = 0
for line in f:
    print(line)
    num += 1
    if num == 25:
        n = 0
        os.system('pause')  # 文件编码有问题

print('no more line')