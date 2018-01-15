# 传递和调用（内建）函数

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 99999)
print(convert(int, myseq))
print(convert(int, myseq))
print(convert(float, myseq))