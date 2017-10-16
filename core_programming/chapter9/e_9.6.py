# 文件比较
import operator # 比较用
f1 = open(input('please input file1 name:'), 'r')
f2 = open(input('please input file2 name:'), 'r')

f1_lines = f1.readlines()
f2_lines = f2.readlines()
smaller_file = f1_lines if len(f1_lines) < len(f2_lines) else f2_lines

for i in range(len(smaller_file)):
    if operator.ne(f1_lines[i], f2_lines[i]):
        print('row is ', i + 1)
        f1_line_len = len(f1_lines[i])
        f2_line_len = len(f2_lines[i])
        smaller_line = f1_line_len if f1_line_len < f2_line_len else f2_line_len
        for j in range(smaller_line):
            if operator.ne(f1_lines[i], f2_lines[i]):
                print('col is ', j + 1)
                break  # 退出j
        break
else:
    if f1_lines == f2_lines:
        print('this two files equal')
    else:
        print('row is ', i + 2)

