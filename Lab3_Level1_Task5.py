def power(a, n):
    if n == 0:
        return 1
    if n > 0:
        return a * power(a, n - 1)
    # n < 0
    return 1 / power(a, -n)

# приклад:
x = float(input("Введіть число a: "))
p = int(input("Введіть степінь n: "))
print("Результат:", power(x, p))
