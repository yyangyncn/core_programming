# 文件访问
f = open(input('please input file name:'), 'r')
n = int(input('please input file lines:'))

for i in range(n):
    print(f.readline())

