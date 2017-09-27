# 99
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "X", j, "=", i * j, "  ", end="")
    print()

print()
n = 9
while n >= 1:
    m = 1
    for m in range(1, n+1):
        print(n, "X", m, "=", n * m, "  ", end="")
        m += 1
    n -= 1
    print()
