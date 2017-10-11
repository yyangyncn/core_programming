# 阶乘
def factorial(num):
    if num == 0:
        return 1
    else:
        factorials.append(num)
        return num * factorial(num - 1)

for eachNum in range(1, 10):
    factorials = []
    print(eachNum, factorial(eachNum), ' * '.join(str(i) for i in factorials))