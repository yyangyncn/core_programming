# 完全数
def isperfect(num):
    factors = []
    count = num // 2
    while count >= 1:
        if num % count == 0:
            factors.append(count)
        count -= 1

    if sum(factors) == num:
        return 1, factors
    else:
        return 0, factors

print(isperfect(6))