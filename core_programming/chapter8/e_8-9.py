# fibo
def fibonacci(num):
    if num in [1, 2]:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

for eachNum in range(1, 10):
    print(eachNum, fibonacci(eachNum))