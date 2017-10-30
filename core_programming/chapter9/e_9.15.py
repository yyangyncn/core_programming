# copy file
file1 = input('file1:')
file2 = input('file2:')

f1 = open(file1, 'r', encoding='GBK')
f2 = open(file2, 'w+')
for line in f1:
    f2.write(line)

f1.close()
f2.close()