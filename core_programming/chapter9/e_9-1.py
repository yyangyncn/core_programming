# 文件过滤
f = open('ReadMe.txt', 'r')

for line in f:
    if line[0] != '#':
        print(line)
    elif '#' in line:
        loc = line.find('#')
        print(line[:loc])

f.close()